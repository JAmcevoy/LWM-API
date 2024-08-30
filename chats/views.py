from rest_framework import generics, permissions
from learnwithme.permissions import IsOwnerOrReadOnly
from .models import Chat
from .serializers import ChatSerializer, ChatDetailSerializer

class ChatList(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filter chats by the 'circle' field based on the URL parameter
        circle_id = self.kwargs.get('circle_id')
        if circle_id:
            return Chat.objects.filter(circle=circle_id)
        return Chat.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChatDetailSerializer

    def get_queryset(self):
        return Chat.objects.all()
