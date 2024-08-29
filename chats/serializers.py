from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    
    class Meta:
        model = Chat
        fields = ['id', 'owner', 'circle', 'content', 'timestamp', 'owner_username']

    def get_owner_username(self, obj):
        return obj.owner.username

class ChatDetailSerializer(ChatSerializer):

    circle = serializers.ReadOnlyField(source='circle.id')