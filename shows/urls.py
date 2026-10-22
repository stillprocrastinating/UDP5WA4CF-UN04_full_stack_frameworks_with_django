from django.urls import path
from shows.views import shows_view, showtime_view

urlpatterns = [
    path('', shows_view, name='shows'),
    path('st2026/', showtime_view, name='showtime'),
]
