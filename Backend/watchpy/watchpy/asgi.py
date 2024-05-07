import os

# Importación de la aplicación ASGI de Django
from django.core.asgi import get_asgi_application

# Configuración del entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watchpy.settings')

# Obtener la aplicación ASGI
application = get_asgi_application()
