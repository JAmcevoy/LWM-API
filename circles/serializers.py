from rest_framework import serializers
from .models import InterestCircle, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'type'
        ]

class InterestCircleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    category = CategorySerializer()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user:
            return request.user == obj.owner
        return False

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
            'is_owner'
        ]
