from rest_framework import generics, permissions
from learnwithme.permissions import IsOwnerOrReadOnly
from .models import Chat
from .serializers import ChatSerializer, ChatDetailSerializer


class ChatList(generics.ListCreateAPIView):

    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Chat.objects.all()
    filterset_fields = ['circle']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChatDetailSerializer
    queryset = Chat.objects.all()
