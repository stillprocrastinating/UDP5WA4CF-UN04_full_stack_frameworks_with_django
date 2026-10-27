from django.urls import path
from shows.views import payment_cancelled, payment_successful, shows_view, showtime_view, stripe_webhook

urlpatterns = [
    path('', shows_view, name='shows'),
    path('£XXX/', payment_cancelled, name='payment-cancelled'),
    path('£££/', payment_successful, name='payment-successful'),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
    path('<product_id>/', showtime_view, name='showtime'),
]
