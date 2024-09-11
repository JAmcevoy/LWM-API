from rest_framework import serializers
from .models import Post
from likes.models import Like

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.

    Includes additional fields to provide details about the post's owner,
    ownership status, likes, and related category information.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    category_name = serializers.ReadOnlyField(source='category.type')
    owner_profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    is_owner = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the post.

        Returns True if the current user is the owner; otherwise, False.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Retrieve the ID of the like associated with the current user for this post.

        Returns the like ID if the user has liked the post, or None if not liked.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id',                  # Unique identifier for the post
            'owner',               # Username of the post owner
            'created_at',          # Timestamp when the post was created
            'updated_at',          # Timestamp when the post was last updated
            'title',               # Title of the post
            'steps',               # Steps or content of the post
            'image_or_video',      # URL to the post's image or video
            'category',            # ID of the category associated with the post
            'is_owner',            # Boolean indicating if the current user is the owner
            'like_id',             # ID of the like by the current user, if any
            'likes_count',         # Total number of likes on the post
            'profile_image',       # URL to the owner's profile image
            'category_name',       # Name of the category associated with the post
            'owner_profile_id'     # ID of the owner's profile
        ]
