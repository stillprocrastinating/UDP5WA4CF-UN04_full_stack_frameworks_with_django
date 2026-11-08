from django.contrib import admin
from shows.models import CheckoutSession, ShippingInfo


# admin.site.register(StripeOnePayment)

admin.site.register(CheckoutSession)
admin.site.register(ShippingInfo)
