# Modelos de Django
from django.db import models

# Modelo de usuario de Django
from django.contrib.auth.models import User

# Modelo para Películas
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    ruta_poster = models.URLField()

    def __str__(self):
        return self.titulo

# Modelo para Series
class Serie(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    ruta_poster = models.URLField()

    def __str__(self):
        return self.titulo

# Modelo para el Perfil de Usuario
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfilusuario"
    )
    biografia = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
