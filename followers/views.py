from rest_framework import generics, permissions
from learnwithme.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    """
    API view to list all followers or create a new follower.

    - GET: Retrieve a list of all followers.
    - POST: Create a new follower, setting the current user as the owner.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        """
        Save the new follower with the current user as the owner.
        """
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete a specific follower.

    - GET: Retrieve a follower by its ID.
    - DELETE: Delete a follower.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
