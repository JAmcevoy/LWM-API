from rest_framework import generics, permissions
from learnwithme.permissions import IsOwnerOrReadOnly
from .models import Chat
from .serializers import ChatSerializer, ChatDetailSerializer

class ChatList(generics.ListCreateAPIView):
    """
    API view to list all chats or create a new chat.
    - GET: List all chats, or filter by `circle_id` if provided.
    - POST: Create a new chat.
    """
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Return a list of chats, optionally filtered by `circle_id`.
        If `circle_id` is not provided, return all chats ordered by creation date.
        """
        circle_id = self.kwargs.get('circle_id')
        if circle_id:
            return Chat.objects.filter(circle=circle_id).order_by('created_at')
        return Chat.objects.all().order_by('created_at')

    def perform_create(self, serializer):
        """
        Save the chat instance with the current user set as the owner.
        """
        serializer.save(owner=self.request.user)

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific chat.
    - GET: Retrieve a chat by its ID.
    - PUT/PATCH: Update a chat.
    - DELETE: Delete a chat.
    """
    serializer_class = ChatDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Return a list of all chats.
        """
        return Chat.objects.all()
