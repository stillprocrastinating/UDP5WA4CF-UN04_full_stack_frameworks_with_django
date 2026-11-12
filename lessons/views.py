from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.timezone import now
from lessons.models import LessonSubscription
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def lessons_view(request):

    subscription = {
        'class_1': 'price_1Ua1kQ643VTaWZ4DNJTNGVbw',
        'class_2': 'price_1Ua1gm643VTaWZ4DAcFsZM52',
        'class_3': 'price_1Ua1lt643VTaWZ4DlP6TPOQC',
        'class_4': 'price_1Ua1nZ643VTaWZ4DbAk2OnNm',
        'class_8': 'price_1Ua1vy643VTaWZ4DUzppEGWk'
    }

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('account_login')}?next={request.get_full_path()}")

        price_id = request.POST.get('price_id')

        subscription = LessonSubscription.objects.filter(user=request.user).first()
        if subscription:
            stripe_subscription = stripe.Subscription.retrieve(subscription.subscription_id)
            item = stripe_subscription['items']['data'][0]
            stripe.Subscription.modify(
                subscription.subscription_id,
                items=[{
                    'id': item['id'],
                    'price': price_id
                }],
                cancel_at_period_end=False
            )
            price = stripe.Price.retrieve(price_id)
            product = stripe.Product.retrieve(price['product'])
            subscription.date_start = now()
            subscription.product_name = product.name
            subscription.price = price['unit_amount'] / 100
            subscription.date_end = None
            subscription.date_cancelled = None
            subscription.save()
            return redirect('subscriptions')
        else:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': price_id,
                        'quantity': 1,
                    }
                ],
                allowed_payment_method_types=['card'],     # payment_method_types
                mode='subscription',
                success_url=request.build_absolute_uri(reverse("subscription-create")) + f'?session_id={{CHECKOUT_SESSION_ID}}',
                cancel_url=request.build_absolute_uri(f'{reverse("lessons")}'),
                customer_email=request.user.email,
                metadata={
                    'user_id': request.user.id
                }
            )

            return redirect(checkout_session.url, code=303)

    context = {'subscription': subscription}

    return render(request, 'lessons/lessons.html', context)


def subscription_create(request):

    checkout_session_id = request.GET.get('session_id', None)
    # create subscription object in database

    session = stripe.checkout.Session.retrieve(checkout_session_id)
    user_id = session.metadata["user_id"]     # session.metadata.get("user_id")
    user = User.objects.get(id=user_id)

    subscription = stripe.Subscription.retrieve(session.subscription)
    price = subscription['items']['data'][0]['price']
    product_id = price['product']
    product = stripe.Product.retrieve(product_id)

    if checkout_session_id:
        LessonSubscription.objects.create(
            user=user,
            customer_id=session.customer,
            subscription_id=session.subscription,
            product_name=product.name,
            price=price['unit_amount'] / 100,
            interval=price['recurring']['interval'],
            date_start=datetime.fromtimestamp(subscription['start_date'])     # datetime.fromtimestamp(subscription['current_period_start'])
        )
    return redirect('subscriptions')


def my_lessons_view(request):

    if not request.user.is_authenticated:
        return redirect('account_login')

    subscription = LessonSubscription.objects.filter(user=request.user).first()

    return render(request, 'lessons/my-lessons.html', {'subscription': subscription})


def subscription_cancel(request, subscription_id):

    subscription = get_object_or_404(
        LessonSubscription, subscription_id=subscription_id, user=request.user
    )

    stripe.Subscription.modify(
        subscription_id,
        cancel_at_period_end=True
    )

    subscription.date_cancelled = now()     # subscription.canceled_at

    stripe_subscription = stripe.Subscription.retrieve(subscription_id)
    subscription.date_end = datetime.fromtimestamp(stripe_subscription['canceled_at'])     # stripe_subscription['current_period_end']

    subscription.save()

    return redirect('subscriptions')
