from .views import profile_edit_view, profile_email_change, profile_email_verify, profile_delete_view, profile_settings_view, profile_view
from django.urls import path


urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='profile-edit'),
    path('email-change/', profile_email_change, name='profile-email-change'),
    path('email-verify/', profile_email_verify, name='profile-email-verify'),
    path('delete/', profile_delete_view, name='profile-delete'),
    path('settings/', profile_settings_view, name='profile-settings'),
    path('signup/', profile_edit_view, name='profile-signup'),
]
