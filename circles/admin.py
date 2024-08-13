from django.contrib import admin
from .models import Category, InterestCircle

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('type',)

@admin.register(InterestCircle)
class InterestCircleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',) 
