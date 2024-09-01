from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from profiles.models import Profile
from followers.models import Follower
from followers.serializers import FollowerSerializer

class FollowProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        if Follower.objects.filter(owner=request.user, followed=profile).exists():
            return Response({'detail': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        Follower.objects.create(owner=request.user, followed=profile)
        return Response({'detail': 'Profile followed.'}, status=status.HTTP_201_CREATED)

class UnfollowProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        follower = Follower.objects.filter(owner=request.user, followed=profile).first()
        if follower:
            follower.delete()
            return Response({'detail': 'Profile unfollowed.'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
