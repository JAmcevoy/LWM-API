from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like

class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.

    Handles serialization of like data and manages unique constraints.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    post_title = serializers.ReadOnlyField(source='post.title')
    owner_profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post', 'post_title', 'owner_profile_id']

    def create(self, validated_data):
        """
        Create a new Like instance.

        Raises a ValidationError if an IntegrityError occurs, 
        indicating a possible duplicate entry.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible duplicate entry'
            })
