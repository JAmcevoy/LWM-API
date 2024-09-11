from rest_framework import generics, permissions
from learnwithme.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    """
    API view to list all likes or create a new like.

    - GET: Retrieve a list of all likes.
    - POST: Create a new like, setting the current user as the owner.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        """
        Save the new like with the current user as the owner.
        """
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete a specific like.

    - GET: Retrieve a like by its ID.
    - DELETE: Delete a like.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
