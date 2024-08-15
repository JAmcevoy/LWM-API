from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'sender', 'circle', 'content', 'timestamp']

class ChatDetailSerializer(ChatSerializer):

    circle = serializers.ReadOnlyField(source='circle.id')