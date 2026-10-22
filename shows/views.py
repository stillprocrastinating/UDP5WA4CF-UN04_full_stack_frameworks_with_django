from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
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
    return render(request, 'shows/payment_successful.html')


def payment_cancelled(request):
    return render(request, 'shows/payment_cancelled.html')
