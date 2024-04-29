# En watchpy/models.py

from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    media_type = models.CharField(max_length=10)  # 'movie' or 'tv'

    def __str__(self):
        return self.title

class Trailer(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)  # YouTube video key

    def __str__(self):
        return f"Trailer for {self.media.title}"
