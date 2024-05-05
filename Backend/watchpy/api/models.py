from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.URLField()

    def __str__(self):
        return self.title

class Serie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    first_air_date = models.DateField()
    poster_path = models.URLField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def add_watched_movie(self, movie):
        WatchedMedia.objects.create(user=self.user, movie=movie)

    def add_watched_series(self, series):
        WatchedMedia.objects.create(user=self.user, series=series)

class WatchedMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    series = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True, blank=True)
    watched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title if self.movie else self.series.title}"

    def media_type(self):
        if self.movie:
            return 'Movie'
        elif self.series:
            return 'Series'

class Media(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.URLField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
