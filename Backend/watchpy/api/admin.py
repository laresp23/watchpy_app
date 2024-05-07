# Importación del módulo de administración de Django
from django.contrib import admin

# Importación de modelos
from .models import Pelicula, Serie, PerfilUsuario

# Registro de Película en el panel de administración
@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_estreno', 'ruta_poster')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha_estreno',)

# Registro de Serie en el panel de administración
@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_estreno', 'ruta_poster')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha_estreno',)

# Registro de PerfilUsuario en el panel de administración
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'biografia', 'avatar', 'creado_en')
    search_fields = ('usuario__username',)
    list_filter = ('creado_en',)
