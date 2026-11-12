from django.urls import path
from lessons.views import lessons_view, my_lessons_view, subscription_cancel, subscription_create


urlpatterns = [
    path('', lessons_view, name='lessons'),
    path(
        'cancel/<subscription_id>',
        subscription_cancel,
        name='subscription-cancel'
    ),
    path('create/', subscription_create, name='subscription-create'),
    path('subscriptions/', my_lessons_view, name='subscriptions')
]
