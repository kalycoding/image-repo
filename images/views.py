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
    def get(self, request):
        queryset = ImageCategory.objects.filter(user=request.user)  
        serializer = ImageCategorySerializer(queryset, many=True)
        return response.Response(serializer.data, status=200)