
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'username', 'about_me', 'created_at', 'main_interest')
    search_fields = ('owner__username', 'username', 'about_me', 'main_interest')