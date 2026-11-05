from django.contrib import admin
from shows.models import CheckoutSession, ProductVariation, ShippingInfo


admin.site.register(ProductVariation)

admin.site.register(CheckoutSession)
admin.site.register(ShippingInfo)
