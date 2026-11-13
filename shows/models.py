from django.contrib.auth.models import User
from django.db import models


class ShippingInfo(models.Model):

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE
    )
    email = models.EmailField()
    phone = models.CharField(blank=True, max_length=20, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    address_line_two = models.CharField(blank=True, max_length=255, null=True)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CheckoutSession(models.Model):

    checkout_id = models.CharField(max_length=255)
    shipping_info = models.ForeignKey(
        ShippingInfo, blank=True, null=True, on_delete=models.SET_NULL
    )
    total_price = models.DecimalField(
        blank=True, decimal_places=2, max_digits=10, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    has_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):

        ci = self.checkout_id
        si = self.shipping_info
        tp = self.total_price
        date = self.created.strftime('%d/%m/%Y')
        hp = self.has_paid

        return f'{ci} - {si} - £{tp} - {date} - Paid: {hp}'
