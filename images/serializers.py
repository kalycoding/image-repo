from django.db.models import fields
from rest_framework import serializers
from .models import (
    ImageCategory, 
    Image
)

class ImageCategorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = ImageCategory
        fields = '__all__'


class ImageUploadSerializer(serializers.ModelSerializer):
    image_category = serializers.ReadOnlyField(source='image_category.name')

    class Meta:
        model = Image
        fields = '__all__'


class DeleteBulkImageSerializer(serializers.Serializer):
    image_id = serializers.ListField(child=serializers.JSONField())