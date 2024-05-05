from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from api.urls import urlpatterns as api_urls
from api.views import (
    Home, Peliculas, Series, DetalleMedia, RegisterUser, LoginUser, 
    LogoutUser, UserList, UserDetail, api_root, mark_movie_as_watched, 
    mark_series_as_watched
)

router = routers.DefaultRouter()

urlpatterns = [
    # API endpoints
    path('api/', include(api_urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/peliculas/', Peliculas.as_view(), name='api-peliculas'),
    path('api/series/', Series.as_view(), name='api-series'),
    path('api/detalle-media/', DetalleMedia.as_view(), name='api-detalle-media'),
    path('api/mark-movie-watched/<int:movie_id>/', mark_movie_as_watched, name='api-mark-movie-watched'),
    path('api/mark-series-watched/<int:series_id>/', mark_series_as_watched, name='api-mark-series-watched'),
    
    # Regular endpoints
    path('', Home.as_view(), name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('detalle-media/', DetalleMedia.as_view(), name='detalle-media'),
    path('peliculas/', Peliculas.as_view(), name='peliculas'),
    path('series/', Series.as_view(), name='series'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    
    # Other URLs
    path('docs/', include_docs_urls(title='API Documentation')),
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
]

handler404 = 'api.views.not_found'
