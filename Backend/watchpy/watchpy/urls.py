from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detalle_media/', views.detalle_media, name='detalle_media'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('series/', views.series, name='series'),
]
