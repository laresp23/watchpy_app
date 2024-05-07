import os

# Importación de la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application

# Configuración del entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watchpy.settings')

# Obtener la aplicación WSGI
application = get_wsgi_application()
