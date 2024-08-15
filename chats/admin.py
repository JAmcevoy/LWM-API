from django.contrib import admin
from .models import Chat

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'circle', 'content', 'timestamp')
    list_filter = ('circle', 'timestamp')
    search_fields = ('content', 'sender__username')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',) 

admin.site.register(Chat, ChatAdmin)
