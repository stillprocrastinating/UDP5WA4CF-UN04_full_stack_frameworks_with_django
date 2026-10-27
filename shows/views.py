from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import StripeOnePayment
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def shows_view(request):
    return render(request, 'shows/shows.html')


def showtime_view(request):

    product_id = 'prod_VUQYxR4lNOuWJY'
    product = stripe.Product.retrieve(product_id)

    prices = stripe.Price.list(product=product_id)
    price = prices.data[0]
    product_price = price.unit_amount / 100

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f'{settings.BASE_URL}{reverse("account_login")}?next={request.get_full_path()}')
        price_id = request.POST.get('price_id')
        quantity = int(request.POST.get('quantity'))
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': price_id,
                    'quantity': quantity,
                }
            ],
            # payment_method_types=['card'],     # deprecated
            mode='payment',
            customer_creation='always',     # change
            success_url=f'{settings.BASE_URL}{reverse("payment-successful")}?session_id={{CHECKOUT_SESSION_ID}}',
            cancel_url=f'{settings.BASE_URL}{reverse("payment-cancelled")}',
        )
        return redirect(checkout_session.url, code=303)     # code=303 prevents checkout_session duplication

    context = {
        'product': product,
        'product_price': product_price,
    }

    return render(request, 'shows/showtime.html', context)


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
