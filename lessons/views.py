from django.conf import settings
from django.shortcuts import redirect, render, reverse
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

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1,
                }
            ],
            allowed_payment_method_types=['card'],     # payment_method_types
            mode='subscription',
            success_url=request.build_absolute_uri(reverse("create-subscription")) + f'?session_id={{CHECKOUT_SESSION_ID}}',
            cancel_url=request.build_absolute_uri(f'{reverse("subscription")}'),
            customer_email=request.user.email,
            metadata={
                'user_id': request.user.id
            }
        )

        return redirect(checkout_session.url, code=303)

    context = {'subscription': subscription}

    return render(request, 'lessons/lessons.html', context)


def create_subscription(request):
    checkout_session_id = request.GET.get('session_id', None)
    # create subscription object in database
    return redirect('my_lessons')


def my_lessons_view(request):
    return render(request, 'lessons/my-lessons.html')
