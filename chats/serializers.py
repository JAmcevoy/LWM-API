from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    """
    Serializer for the Chat model to handle serialization of chat data.
    """
    # Read-only field to display the owner's username
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    # Read-only field to display the chat circle's name
    chat_circle_name = serializers.ReadOnlyField(source='circle.name')
    # Ensure the timestamp shows time.
    timestamp = serializers.DateTimeField(format="%d-%b-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'owner', 'circle', 'content', 'timestamp', 'owner_username', 'chat_circle_name']

    def get_owner_username(self, obj):
        """
        Return the username of the chat owner.
        """
        return obj.owner.username

class ChatDetailSerializer(ChatSerializer):
    """
    Serializer for detailed view of the Chat model, extending ChatSerializer.
    Includes circle ID as a read-only field.
    """
    # Read-only field to display the circle's ID
    circle = serializers.ReadOnlyField(source='circle.id')
