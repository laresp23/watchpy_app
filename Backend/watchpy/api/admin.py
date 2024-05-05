from django.contrib import admin
from .models import UserProfile, Movie, Serie, WatchedMedia

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar', 'created_at')
    search_fields = ('user__username', 'user__email', 'bio')
    list_filter = ('created_at',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'overview', 'release_date', 'poster_path')
    search_fields = ('title', 'overview')
    list_filter = ('release_date',)

@admin.register(Serie)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'overview', 'first_air_date', 'poster_path')
    search_fields = ('title', 'overview')
    list_filter = ('first_air_date',)

@admin.register(WatchedMedia)
class WatchedMediaAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_media_title', 'watched_at')
    search_fields = ('user__username', 'movie__title', 'series__title')  # Cambiado de 'media__title'
    list_filter = ('watched_at',)

    def get_media_title(self, obj):
        if obj.movie:
            return obj.movie.title
        elif obj.series:
            return obj.series.title
        else:
            return "Unknown"

    get_media_title.short_description = 'Media Title'
