from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from shows.cart import Cart
from shows.forms import ShippingForm
from shows.models import CheckoutSession, ProductVariation, ShippingInfo
from shows.utils import create_checkout_session, get_product_details
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def shows_view(request):

    # del request.session[settings.CART_SESSION_ID]

    products_list = stripe.Product.list()
    products = []

    for product in products_list['data']:
        if product['metadata']['category'] == "show_recording":     # product.get('metadata', {}).get('category')
            products.append(get_product_details(product, None))

    return render(request, 'shows/shows.html', {'products': products})


def showtime_view(request, product_id):

    disk = request.GET.get('disk') or 'DVD'

    product_variation = ProductVariation.objects.filter(product_id=product_id).first()
    product = stripe.Product.retrieve(product_id)
    product_details = get_product_details(product, disk)

    cart = Cart(request)
    product_details['in_cart'] = product_id in cart.cart_session

    context = {
        'product': product_details,
        'product_variation': product_variation,
        'disk': disk
    }

    return render(request, 'shows/showtime.html', context)


def add_to_cart(request, product_id):

    product = stripe.Product.retrieve(product_id)

    disk = request.GET.get('disk') or ('dvd')
    if disk == 'dvd':
        disk = disk.upper()
    else:
        disk = disk.capitalize()

    cart = Cart(request)
    cart.add(product_id, disk=disk)
    # print(cart.cart_session)

    product_details = get_product_details(product, disk)
    product_details['in_cart'] = product_id in cart.cart_session

    response = render(
        request,
        'shows/partials/cart-button.html',
        {'product': product_details}
    )
    response['HX-Trigger'] = 'hx_menu_cart'

    return response


def hx_menu_cart(request):
    return render(request, 'shows/partials/menu-cart.html')


def cart_view(request):

    quantity_range = list(range(1, 11))

    return render(
        request, 'shows/cart.html', {'quantity_range': quantity_range}
    )


def remove_from_cart(request, product_id):

    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart')


def hx_checkout(request, item_id):

    quantity = int(request.POST.get('quantity', 1))
    disk = request.POST.get('disk')
    cart = Cart(request)
    product_id = cart.cart_session.get(item_id)['product_id']
    cart.add(product_id, quantity, item_id=item_id)

    product = stripe.Product.retrieve(product_id)
    product_details = get_product_details(product, disk)
    product_details['total_price'] = product_details['price'] * quantity
    product_details['item_id'] = item_id

    response = render(
        request, 'shows/partials/checkout-total.html', {'product': product}
    )
    response['HX-Trigger'] = 'hx_menu_cart'

    return response


@login_required
def checkout_view(request):

    shipping_info = ShippingInfo.objects.filter(user=request.user).first()

    if shipping_info:
        form = ShippingForm(instance=shipping_info)
    else:
        form = ShippingForm(initial={'email': request.user.email})

    if request.method == 'POST':

        form = ShippingForm(request.POST, instance=shipping_info)

        if form.is_valid():

            shipping_info = form.save(commit=False)
            shipping_info.user = request.user
            shipping_info.email = form.cleaned_data['email'].lower()
            shipping_info.save()

            cart = Cart(request)

            checkout_session = create_checkout_session(
                cart, shipping_info.email
            )

            CheckoutSession.objects.create(
                checkout_id=checkout_session.id,
                shipping_info=shipping_info,
                total_price=cart.get_total_price()
                # has_paid=False by default
            )

            return redirect(checkout_session.url, code=303)

    return render(request, 'shows/checkout.html', {'form': form})


def payment_successful(request):

    checkout_session_id = request.GET.get('session_id', None)

    if checkout_session_id:
        session = stripe.checkout.Session.retrieve(checkout_session_id)
        customer_id = session.customer
        customer = stripe.Customer.retrieve(customer_id)

        if settings.CART_SESSION_ID in request.session:
            del request.session[settings.CART_SESSION_ID]

        if settings.DEBUG:
            checkout = CheckoutSession.objects.get(
                checkout_id=checkout_session_id
            )
            checkout.has_paid = True
            checkout.save()

    return render(
        request, 'shows/payment_successful.html', {'customer': customer}
    )


def payment_cancelled(request):
    return render(request, 'shows/payment_cancelled.html')


@require_POST
@csrf_exempt
def stripe_webhook(request):

    payload = request.body     # JSON data
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']     # stripe origin verification
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET     # stripe webhook key
    e = None

    try:
        e = stripe.Webhook.construct_event(
            payload, signature_header, endpoint_secret,
        )
    except:
        return HttpResponse(status=400)     # bad request error

    if e['type'] == 'checkout.session.completed':
        session = e['data']['object']
        checkout_session_id = session.get('id')
        checkout = CheckoutSession.objects.get(
            stripe_checkout_id=checkout_session_id
        )
        checkout.has_paid = True
        checkout.save()

    return HttpResponse(status=200)     # success
