from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .cart import Cart
from .models import StripeOnePayment
from .utils import get_product_details
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def shows_view(request):
    products_list = stripe.Product.list()
    products = []

    for product in products_list['data']:
        # if product.get('metadata', {}).get('category') == "show_recording":     # .get() AttributeError: dict
        if product['metadata']['category'] == "show_recording":
            products.append(get_product_details(product))

    return render(request, 'shows/shows.html', {'products': products})


def showtime_view(request, product_id):

    product = stripe.Product.retrieve(product_id)
    product_details = get_product_details(product)

    cart = Cart(request)
    product_details['in_cart'] = product_id in cart.cart_session

    return render(request, 'shows/showtime.html', {'product': product_details})


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    # print(cart.cart_session)
    return redirect('showtime', product_id)


def payment_successful(request):
    checkout_session_id = request.GET.get('session_id', None)
    if checkout_session_id:
        session = stripe.checkout.Session.retrieve(checkout_session_id)
        customer_id = session.customer
        customer = stripe.Customer.retrieve(customer_id)

        line_item = stripe.checkout.Session.list_line_items(checkout_session_id).data[0]
        StripeOnePayment.objects.get_or_create(
            user=request.user,
            stripe_customer_id=customer_id,
            stripe_checkout_id=checkout_session_id,
            stripe_product_id=line_item.price.product,
            product_name=line_item.description,
            quantity=line_item.quantity,
            price=line_item.price.unit_amount / 100,
            currency=line_item.price.currency,
            has_paid=True
        )

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
        user_payment = StripeOnePayment.objects.get(stripe_checkout_id=checkout_session_id)
        user_payment.has_paid = True
        user_payment.save()

    return HttpResponse(status=200)     # success
