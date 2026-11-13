# Entity Relationship Diagram


## c_users

### Profile

|Key|Name|Type|
|-|-|-|
|OneToOneField|user|User, on_delete=models.CASCADE|
||image|ImageField(blank=True, null=True, upload_to="avatars/")|
||displayname|CharField(blank=True, max_length=20, null=True)|
||info|TextField(blank=True, null=True)|


## lessons

### LessonSubscription

|Key|Name|Type|
|-|-|-|
|ForeignKey|user|User, on_delete=models.CASCADE|
||customer_id|CharField(max_length=255)|
||subscription_id|CharField(max_length=255, unique=True)|
||product_name|CharField(max_length=255)|
||price|IntegerField()|
||interval|CharField(max_length=50, default="week")|
||date_start|DateTimeField(auto_now_add=True)|
||date_end|DateTimeField(blank=True, null=True)|
||date_cancelled|DateTimeField(blank=True, null=True)|


## shows

### ShippingInfo

|Key|Name|Type|
|-|-|-|
|ForeignKey|user|User, blank=True, null=True, on_delete=models.CASCADE|
||email|EmailField()|
||phone|CharField(blank=True, max_length=20, null=True)|
||first_name|CharField(max_length=100)|
||last_name|CharField(max_length=100)|
||address|CharField(max_length=255)|
||address_line_two|CharField(blank=True, max_length=255, null=True)|
||city|CharField(max_length=100)|
||postcode|CharField(max_length=10)|


### CheckoutSession

|Key|Name|Type|
|-|-|-|
||checkout_id|CharField(max_length=255)|
|ForeignKey|shipping_info|ShippingInfo, blank=True, null=True, on_delete=models.SET_NULL|
||total_price|DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)|
||created|DateTimeField(auto_now_add=True)|
||has_paid|BooleanField(default=False)|

---
---

# Initial plans

## shows

### StripeOnePayment

|Key|Name|Type|
|-|-|-|
|ForeignKey|user|User, on_delete=models.CASCADE|
||stripe_customer_id|CharField(max_length=255)|
||stripe_checkout_id|CharField(max_length=255)|
||stripe_product_id|CharField(max_length=255)|
||product_name|CharField(max_length=255)|
||quantity|IntegerField(default=1)|
||price|DecimalField(decimal_places=2, max_digits=10)|
||currency|CharField(max_length=3)|
||has_paid|BooleanField(default=False)|
