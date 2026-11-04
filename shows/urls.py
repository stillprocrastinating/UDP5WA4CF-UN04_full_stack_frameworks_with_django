from django.urls import path
from shows.views import add_to_cart, cart_view, hx_checkout, hx_menu_cart, payment_cancelled, payment_successful, shows_view, showtime_view, stripe_webhook

urlpatterns = [
    path('', shows_view, name='shows'),
    path('£XXX/', payment_cancelled, name='payment-cancelled'),
    path('£££/', payment_successful, name='payment-successful'),
    path('cart/', cart_view, name='cart'),
    path('cart/<product_id>/', add_to_cart, name='add-to-cart'),
    path('hx_checkout/<product_id>/', hx_checkout, name='hx-checkout'),
    path('hx_menu_cart/', hx_menu_cart, name='hx-menu-cart'),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
    path('<product_id>/', showtime_view, name='showtime'),
]
