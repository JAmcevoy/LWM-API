from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'username', 'about_me', 'created_at', 'main_interest')
    search_fields = ('owner__username', 'username', 'about_me')
    list_filter = ('main_interest',)