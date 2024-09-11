from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from learnwithme.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    """
    API view to list all profiles with options for filtering and ordering.

    - GET: Retrieve a list of profiles with counts for posts, followers, and following.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),           # Count distinct posts by the owner
        followers_count=Count('owner__followed', distinct=True),   # Count distinct followers of the owner
        following_count=Count('owner__following', distinct=True)   # Count distinct profiles the owner is following
    ).order_by('-created_at')  # Order profiles by creation date, most recent first
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,   # Allows ordering of results
        DjangoFilterBackend,      # Allows filtering of results
    ]
    filterset_fields = [
        'owner__following__followed__profile',  # Filter profiles based on who the owner is following
        'owner__followed__owner__profile',      # Filter profiles based on who follows the owner
    ]
    ordering_fields = [
        'posts_count',                         # Order profiles by the number of posts
        'followers_count',                     # Order profiles by the number of followers
        'following_count',                     # Order profiles by the number of following
        'owner__following__created_at',        # Order profiles by the creation date of following relationships
        'owner__followed__created_at',         # Order profiles by the creation date of follower relationships
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve or update a specific profile.

    - GET: Retrieve a profile by its ID.
    - PUT/PATCH: Update a profile if the current user is the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),           # Count distinct posts by the owner
        followers_count=Count('owner__followed', distinct=True),   # Count distinct followers of the owner
        following_count=Count('owner__following', distinct=True)   # Count distinct profiles the owner is following
    ).order_by('-created_at')  # Order profiles by creation date, most recent first
    serializer_class = ProfileSerializer
