from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'owner', 'circle', 'content', 'timestamp']

    def get_owner_username(self, obj):
        return obj.owner.username

class ChatDetailSerializer(ChatSerializer):

    circle = serializers.ReadOnlyField(source='circle.id')