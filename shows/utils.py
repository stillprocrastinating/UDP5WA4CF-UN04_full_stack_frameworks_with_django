from django.conf import settings
from django.urls import reverse
from shows.models import ProductVariation
import stripe


def get_product_details(product, disk=None):

    product_variation = ProductVariation.objects.filter(product_id=product.id).first()

    if product_variation:
        price = product_variation.get_price(disk)
    else:
        price_id = product.default_price
        price = stripe.Price.retrieve(price_id)

    product_details = {
        'id': product['id'],
        'name': product['name'],
        'image': product['images'][0],
        'description': product['description'],
        'price_in_pence': price['unit_amount'],
        'price': price['unit_amount'] / 100,
    }

    return product_details


def create_checkout_session(cart, customer_email):

    line_items = []
    sBU = settings.BASE_URL
    rps = reverse("payment-successful")

    for item in cart:

        options = []

        if item.get('disk') is not None:
            options.append(f"Disk type: {item['disk']}")

        description = ", ".join(options) if options else item['description']

        line_items.append({
            'price': {
                'currency': 'gbp',     # 'usd'
                'product_data': {
                    'name': item['name'],
                    'description': description,
                    'images': [item['image']]
                },
                'unit_amount': item['price_in_pence']
            },
            'quantity': item['quantity']
        })

    checkout_session = stripe.checkout.Session.create(
        line_items=line_items,
        allowed_payment_method_types=['card'],     # payment_method_types
        mode='payment',
        customer_creation='always',
        success_url=f'{sBU}{rps}?session_id={{CHECKOUT_SESSION_ID}}',
        cancel_url=f'{sBU}{reverse("cart")}',
        customer_email=customer_email
    )

    return checkout_session
