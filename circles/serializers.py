from rest_framework import serializers
from .models import InterestCircle, Category

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = ['id', 'type']

class InterestCircleSerializer(serializers.ModelSerializer):
    """
    Serializer for the InterestCircle model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.ReadOnlyField(source='category.type')
    owner_profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the interest circle.
        """
        request = self.context.get('request')
        return request and request.user == obj.owner

    class Meta:
        model = InterestCircle
        fields = [
            'id',
            'name',
            'description',
            'category',
            'created_at',
            'updated_at',
            'owner',
            'is_owner',
            'owner_profile_id',
            'category_name'
        ]
