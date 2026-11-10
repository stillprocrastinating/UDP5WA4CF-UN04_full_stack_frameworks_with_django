from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class LessonSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=255)
    subscription_id = models.CharField(max_length=255, unique=True)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    interval = models.CharField(max_length=50, default="week")
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_cancelled = models.DateTimeField(blank=True, null=True)

    @property
    def is_active(self):
        if self.date_end:
            if now() < self.date_end:
                return True
            else:
                return False
        else:
            return True

    @property
    def l_class(self):
        class_mapping = {
            'Class 1': 1,
            'Class 2': 2,
            'Class 3': 3,
            'Class 4': 4,
            'Class 8': 8
        }
        l_class = class_mapping.get(self.product_name, None)

        return l_class

    def __str__(self):
        return f"{self.user.username} - {self.product_name} - Active: {self.is_active}"

    def next_billing_date(self):
        if self.is_active:
            if self.interval == 'week':
                next_billing_date = self.date_start + relativedelta(weeks=1)
            elif self.interval == 'month':
                next_billing_date = self.date_start + relativedelta(months=1)
            else:
                next_billing_date = self.date_start + relativedelta(years=1)
        else:
            next_billing_date = None

        return next_billing_date
