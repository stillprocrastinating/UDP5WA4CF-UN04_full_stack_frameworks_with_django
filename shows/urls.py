from django.urls import path
from shows.views import payment_cancelled, payment_successful, shows_view, showtime_view

urlpatterns = [
    path('', shows_view, name='shows'),
    path('£XXX/', payment_cancelled, name='payment-cancelled'),
    path('£££/', payment_successful, name='payment-successful'),
    path('st2026/', showtime_view, name='showtime'),
]
