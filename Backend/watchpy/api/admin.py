# myapp/admin.py
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'created_at')
    search_fields = ('user__username', 'user__email', 'bio')
    list_filter = ('created_at',)
