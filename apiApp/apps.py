from django.apps import AppConfig


class ApiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apiApp'
    #--------------------- scheduler ------------------------------
    def ready(self):
        from apiApp.jobs import updater
        updater.start()