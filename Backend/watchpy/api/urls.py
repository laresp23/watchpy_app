# Módulo de URLs de Django
from django.urls import path

# Importación de las vistas del proyecto
from . import views

# Definición de las URL patterns
urlpatterns = [
    # Ruta para la raíz de la API
    path('raiz-api/', views.raiz_api, name='raiz_api'),
]
