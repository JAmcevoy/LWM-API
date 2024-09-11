from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current user, extending UserDetailsSerializer.

    Adds additional fields for the user's profile information.
    """
    # Read-only field for the user's profile ID
    profile_id = serializers.ReadOnlyField(source='profile.id')
    # Read-only field for the URL of the user's profile image
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """
        Meta class to include additional fields in the serialized data.
        """
        fields = UserDetailsSerializer.Meta.fields + ('profile_id', 'profile_image')
