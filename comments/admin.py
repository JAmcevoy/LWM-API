from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'text', 'created_at', 'updated_at')
    list_filter = ('owner', 'created_at')
    search_fields = ('content', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(Comment, CommentAdmin)

