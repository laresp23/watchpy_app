# Configuración de la aplicación Django
from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # Método para ejecutar acciones cuando la aplicación está lista 
    def ready(self):
        import api.signals
