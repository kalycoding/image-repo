from django.db.models import query
from django.shortcuts import render
from rest_framework import (
    response,
    generics,
    permissions,
    serializers,
    views
)
import rest_framework

from .serializers import (
    DeleteBulkImageSerializer,
    ImageCategorySerializer,
    ImageSerializer,
    ImageUploadSerializer
)
from .models import (
    ImageCategory,
    Image
)
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyImage
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

    
class ImageCategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageCategory.objects.all()
    serializer_class = ImageCategorySerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

class SingleImageUploadView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class=ImageUploadSerializer
    def post(self, request, pk):
        try:
            image_cat = ImageCategory.objects.get(pk=pk)
        except ImageCategory.DoesNotExist:
            return response.Response({'error':'Not found'}, status=404)
        if request.user == image_cat.user:
            serializer = ImageUploadSerializer(data=request.data)
            if serializer.is_valid():
                image = Image(
                    name=request.data['name'],
                    description=request.data['description'],
                    image_category=image_cat,
                    public_image=request.data['public_image']
                )
                image.save()
                return response.Response('images save')
            return response.Response(serializer.errors, status=400)
        return response.Response({'status':'Not your category'}, status=403)

class BulkImageUpload(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        try:
            image_cat = ImageCategory.objects.get(pk=pk)
        except ImageCategory.DoesNotExist:
            return response.Response({'error':'Not found'}, status=404)
        if request.user == image_cat.user:
            data = request.data
            files = request.FILES
            print(files)
            for file in files:
                print(files[file])
                image = Image(
                image_category=image_cat,
                name=data['name'],
                description=data['description'],
                file=files[file]
                )
                image.save()
            return response.Response('images save')
        return response.Response({'status':'Not your category'}, status=403)

class DeleteSingleImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageUploadSerializer
    permission_classes = [IsOwnerOrReadOnlyImage, permissions.IsAuthenticated]

class DeleteBulkImage(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DeleteBulkImageSerializer
    def delete(self, request):
        verified_image_user_id = []
        data = request.data

        for image in data:
            try:
                image = Image.objects.get(pk=image['id'])
            except Image.DoesNotExist:
                return response.Response(status=404)

            if image.image_category.user == request.user:
                verified_image_user_id.append(image)
        
        for image_id in verified_image_user_id:
            image_id.delete()
        return response.Response(status=204)

class DeleteAllImagesInCategory(generics.DestroyAPIView):
    def delete(self, request, pk):
        try:
            image_cat = ImageCategory.objects.get(pk=pk)
        except ImageCategory.DoesNotExist:
            return response.Response({'error':'Not found'}, status=404)
        images = image_cat.image_set.all()
        images.delete()
        return response.Response(status=204)
class ImageListView(generics.ListAPIView):
    def get(self,request, pk):
        try:
            image_cat = ImageCategory.objects.get(pk=pk)
        except ImageCategory.DoesNotExist:
            return response.Response({'error':'Not found'}, status=404)

        images = image_cat.image_set.all()
        serializer = ImageUploadSerializer(images, many=True)
        return response.Response(serializer.data, status=200)

class ImageVies(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer