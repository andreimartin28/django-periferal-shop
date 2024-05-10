from django.apps import AppConfig


class ShopappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopapp'

    def ready(self):
        import shopapp.signals
