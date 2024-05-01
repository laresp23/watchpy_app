from django.contrib import admin
from .models import Media, Trailer, UserProfile

# Registra los modelos en el panel de administración de la aplicación
admin.site.register(Media)
admin.site.register(Trailer)
admin.site.register(UserProfile)