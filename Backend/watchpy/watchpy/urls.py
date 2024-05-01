from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from api.urls import urlpatterns as api_urls
from api.views import Home, Peliculas, Series, DetalleMedia, RegisterUser, LoginUser, LogoutUser, UserList, UserDetail, api_root

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='API Documentation')),
    path('api/', include(api_urls)),  # Incluir las URLs de tu aplicación aquí
    path('', Home.as_view(), name='home'),
    path('peliculas/', Peliculas.as_view(), name='peliculas'),
    path('series/', Series.as_view(), name='series'),
    path('detalle-media/', DetalleMedia.as_view(), name='detalle-media'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('', api_root, name='api-root'),
]


# Rutas que solo estarán disponibles a través de la API
urlpatterns += [
    path('api/peliculas/', Peliculas.as_view(), name='peliculas'),
    path('api/series/', Series.as_view(), name='series'),
    path('api/detalle-media/', DetalleMedia.as_view(), name='detalle-media'),
]