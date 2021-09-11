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

