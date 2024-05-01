from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    media_type = models.CharField(max_length=10)  # 'movie' or 'tv'

    def __str__(self):
        return self.title

    def to_dict(self):
        """Convierte el objeto Media a un diccionario."""
        return {
            'id': self.id,
            'title': self.title,
            'overview': self.overview,
            'poster_path': self.poster_path,
            'media_type': self.media_type
        }

class Trailer(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)  # YouTube video key

    def __str__(self):
        return f"Trailer for {self.media.title}"

    def to_dict(self):
        """Convierte el objeto Trailer a un diccionario."""
        return {
            'id': self.id,
            'key': self.key
        }

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    bio = models.TextField(blank=True)  # Biografía del usuario
    birth_date = models.DateField(null=True, blank=True)  # Fecha de nacimiento del usuario
    first_name = models.CharField(max_length=30, blank=True)  # Nombre del usuario
    last_name = models.CharField(max_length=150, blank=True)  # Apellido del usuario
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  # Imagen de perfil del usuario

    def __str__(self):
        return self.user.username  # Nombre de usuario del perfil
