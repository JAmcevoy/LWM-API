from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from learnwithme.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """
    API view to list all posts or create a new post.

    - GET: Retrieve a list of posts with optional filtering, searching, and ordering.
    - POST: Create a new post, setting the current user as the owner.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',  # Filter posts by the profile of followed owners
        'likes__owner__profile',            # Filter posts by the profile of users who liked the post
        'owner__profile',                   # Filter posts by the profile of the post owner
    ]
    search_fields = [
        'owner__username',  # Search posts by the username of the owner
        'title',            # Search posts by title
    ]
    ordering_fields = [
        'likes_count',      # Order posts by the number of likes
        'likes__created_at', # Order posts by the creation date of likes
    ]

    def perform_create(self, serializer):
        """
        Save the new post with the current user as the owner.
        """
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific post.

    - GET: Retrieve a post by its ID.
    - PUT/PATCH: Update a post.
    - DELETE: Delete a post.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
