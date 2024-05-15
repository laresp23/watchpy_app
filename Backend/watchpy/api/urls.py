from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    Home,
    Peliculas,
    Series,
    PeliculasPopulares,
    SeriesPopulares,
    DetallePelicula,
    DetalleSerie,
    RegistrarUsuario,
    IniciarSesionUsuario,
    CerrarSesionUsuario,
    ListaUsuarios,
    DetalleUsuario,
    PerfilUsuarioAPIView,
    raiz_api,
    no_encontrado,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView
)
 
urlpatterns = [
    path('', raiz_api, name='raiz-api'),
    path('home/', Home.as_view(), name='home'),
    path('peliculas/', Peliculas.as_view(), name='peliculas'),
    path('series/', Series.as_view(), name='series'),
    path('peliculas-populares/', PeliculasPopulares.as_view(), name='peliculas-populares'),
    path('series-populares/', SeriesPopulares.as_view(), name='series-populares'),
    path('peliculas/<int:pk>/', DetallePelicula.as_view(), name='detalle-pelicula'),
    path('series/<int:pk>/', DetalleSerie.as_view(), name='detalle-serie'),
    path('registrar/', RegistrarUsuario.as_view(), name='registrar'),
    path('iniciar-sesion/', IniciarSesionUsuario.as_view(), name='iniciar-sesion'),
    path('cerrar-sesion/', CerrarSesionUsuario.as_view(), name='cerrar-sesion'),
    path('usuarios/', ListaUsuarios.as_view(), name='lista-usuarios'),
    path('usuarios/<int:pk>/', DetalleUsuario.as_view(), name='detalle-usuario'),
    path('perfil-usuario/', PerfilUsuarioAPIView.as_view(), name='perfil-usuario-list'),
    path('perfil-usuario/<int:perfil_id>/', PerfilUsuarioAPIView.as_view(), name='perfil-usuario-detail'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('404/', no_encontrado, name='no_encontrado'),
]
