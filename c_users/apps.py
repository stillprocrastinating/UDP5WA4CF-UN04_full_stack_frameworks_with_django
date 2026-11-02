from django.apps import AppConfig


class AUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'c_users'

    def ready(self):
        import c_users.signals
