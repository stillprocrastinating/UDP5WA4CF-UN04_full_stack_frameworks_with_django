from django.urls import path
from lessons.views import create_subscription, lessons_view, my_lessons_view


urlpatterns = [
    path('', lessons_view, name='lessons'),
    path('create/', create_subscription, name='create-subscription'),
    path('subscriptions/', my_lessons_view, name='subscriptions')
]
