from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="profiles", verbose_name="Usuario"
    )
    profile_name = models.CharField(max_length=100, verbose_name="Perfil", default="Mi Perfil")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Avatar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")

    # Campos adicionales para perfiles al estilo de Netflix
    age = models.PositiveIntegerField(verbose_name="Edad", blank=True, null=True)
    preferred_language = models.CharField(max_length=50, verbose_name="Idioma Preferido", blank=True)
    favorite_movies = models.ManyToManyField('Pelicula', verbose_name="Películas Favoritas", blank=True)
    favorite_series = models.ManyToManyField('Serie', verbose_name="Series Favoritas", blank=True)

    def __str__(self):
        return f"{self.profile_name} - {self.user.username}"

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
        ordering = ['user', 'profile_name']

class Pelicula(models.Model):
    title = models.CharField(max_length=255,default="", verbose_name="Título")
    overview = models.TextField(verbose_name="Descripción", default="", blank=True)
    release_date = models.DateField(verbose_name="Fecha de Estreno", null=True, blank=True)
    poster_path = models.URLField(verbose_name="URL del Póster", blank=True)
    vote_average = models.FloatField(verbose_name="Calificación", default=0.0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ['title']


class Serie(models.Model):
    name = models.CharField(max_length=255,default="", verbose_name="Nombre")
    overview = models.TextField(verbose_name="Descripción", default="", blank=True)
    release_date = models.DateField(verbose_name="Fecha de Estreno", null=True, blank=True)
    poster_path = models.URLField(verbose_name="URL del Póster", blank=True)
    vote_average = models.FloatField(verbose_name="Calificación", default=0.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Series"
        ordering = ['name']
