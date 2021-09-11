from django.db.models import query
from django.shortcuts import render
from rest_framework import (
    response,
    generics,
    permissions,
    serializers
)

from .serializers import (
    ImageCategorySerializer
)
from .models import (
    ImageCategory,
    Image
)
# Create your views here.

class ImageCategoryViewList(generics.ListAPIView):
    serializer_class = ImageCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        queryset = ImageCategory.objects.filter(user=request.user)  
        serializer = ImageCategorySerializer(queryset, many=True)
        return response.Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = ImageCategorySerializer(data=request.data)
        if serializer.is_valid():
            image_category = ImageCategory(
                name=request.data['name'],
                description=request.data['description'],
                user=request.user
            )
            image_category.save()
            return response.Response(image_category.to_json(), status=201)
        return response.Response(serializer.errors, status=400)

    