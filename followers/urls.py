from django.urls import path
from followers.views import FollowProfile, UnfollowProfile

urlpatterns = [
    path('profiles/<int:pk>/follow/', FollowProfile.as_view(), name='follow-profile'),
    path('profiles/<int:pk>/unfollow/', UnfollowProfile.as_view(), name='unfollow-profile'),
]
