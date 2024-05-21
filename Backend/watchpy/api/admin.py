from django.contrib import admin
from .models import PerfilUsuario, Pelicula, Serie

# Registro de PerfilUsuario en el panel de administración
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_name', 'bio', 'avatar', 'created_at')
    search_fields = ('user__username', 'profile_name')
    list_filter = ('created_at', 'age', 'preferred_language')
    filter_horizontal = ('favorite_movies', 'favorite_series') 

    fieldsets = (
        (None, {
            'fields': ('user', 'profile_name', 'avatar')
        }),
        ('Información Adicional', {
            'fields': ('bio', 'age', 'preferred_language', 'favorite_movies', 'favorite_series'),
            'classes': ('collapse',)  
        }),
    )

# Registro de Pelicula en el panel de administración
@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'vote_average')
    search_fields = ('title',)
    list_filter = ('release_date', 'vote_average')

# Registro de Serie en el panel de administración
@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'vote_average')
    search_fields = ('name',)
    list_filter = ('release_date', 'vote_average')

