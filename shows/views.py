from django.conf import settings
from django.shortcuts import render
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

    context = {
        'product': product,
        'product_price': product_price,
    }

    return render(request, 'shows/showtime.html', context)
