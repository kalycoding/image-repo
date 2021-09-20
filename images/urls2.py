from django.conf.urls import url
from django.urls import path
from .views import DeleteSingleImage, DeleteBulkImage, ImageVies

urlpatterns = [
    path('public/', ImageVies.as_view(), name='image-category'),
    path('<int:pk>/', DeleteSingleImage.as_view(), name='delete_image'),
    path('delete/bulk/', DeleteBulkImage.as_view())
]
