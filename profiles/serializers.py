from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.

    Includes fields for profile details, ownership status, and relationship data.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    interest_name = serializers.ReadOnlyField(source='main_interest.type')
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the profile.

        Returns True if the current user is the owner; otherwise, False.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Retrieve the ID of the following relationship between the current user and the profile's owner.

        Returns the following ID if the user is following the profile's owner; otherwise, None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',                 # Unique identifier for the profile
            'owner',              # Username of the profile owner
            'created_at',         # Timestamp when the profile was created
            'updated_at',         # Timestamp when the profile was last updated
            'username',           # Username associated with the profile
            'about_me',           # Information about the user
            'main_interest',      # ID of the user's main interest
            'interest_name',      # Name of the main interest
            'image',              # URL of the profile image
            'is_owner',           # Boolean indicating if the current user is the profile owner
            'following_id',       # ID of the following relationship, if any
            'posts_count',        # Total number of posts by the user
            'followers_count',    # Total number of followers the user has
            'following_count'     # Total number of users the user is following
        ]
