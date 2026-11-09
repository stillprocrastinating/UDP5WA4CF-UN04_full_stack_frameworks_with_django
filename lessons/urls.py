from django.urls import path
from lessons.views import lessons_view


urlpatterns = [
    path('', lessons_view, name='lessons')
]
