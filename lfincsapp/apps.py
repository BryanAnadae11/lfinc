from django.apps import AppConfig


class LfincsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lfincsapp'

    def ready(self):
    	import lfincsapp.signals
