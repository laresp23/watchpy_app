from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from api.views import (
    DetallePelicula,
    DetalleSerie,
    Home,
    Peliculas,
    Series,
    RegistrarUsuario,
    IniciarSesionUsuario,
    CerrarSesionUsuario,
    ListaUsuarios,
    DetalleUsuario,
    no_encontrado,
)

# Definición de las URL patterns
urlpatterns = [
    path("", Home.as_view(), name="home"),

    # API
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/docs/", include_docs_urls(title="API Documentation")),

    # Admin
    path("admin/", admin.site.urls),

    # Vistas relacionadas con películas y series
    path("api/peliculas/", Peliculas.as_view(), name="lista-peliculas"),
    path("api/series/", Series.as_view(), name="lista-series"),
    path("api/pelicula/<int:pk>/", DetallePelicula.as_view(), name="detalle-pelicula"),
    path("api/serie/<int:pk>/", DetalleSerie.as_view(), name="detalle-serie"),

    # Autenticación de usuarios
    path("api/usuarios/", ListaUsuarios.as_view(), name="lista_usuarios"),
    path("api/usuarios/<int:pk>/", DetalleUsuario.as_view(), name="detalle_usuario"),
    path("api/registrar/", RegistrarUsuario.as_view(), name="registrar_usuario"),
    path("api/iniciar-sesion/", IniciarSesionUsuario.as_view(), name="iniciar_sesion_usuario"),
    path("api/cerrar-sesion/", CerrarSesionUsuario.as_view(), name="cerrar_sesion_usuario"),
]

# Manejador personalizado para error 404
handler404 = no_encontrado
