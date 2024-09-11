from rest_framework import generics, permissions
from learnwithme.permissions import IsOwnerOrReadOnly
from .models import Chat
from .serializers import ChatSerializer, ChatDetailSerializer

class ChatList(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        circle_id = self.kwargs.get('circle_id')
        if circle_id:
            return Chat.objects.filter(circle=circle_id)
        return Chat.objects.all().order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChatDetailSerializer

    def get_queryset(self):
        return Chat.objects.all()
