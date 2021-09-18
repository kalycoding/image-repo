from django.conf.urls import url
from django.urls import path
from .views import DeleteSingleImage, DeleteBulkImage

urlpatterns = [
    path('<int:pk>/', DeleteSingleImage.as_view(), name='delete_image'),
    path('delete/bulk/', DeleteBulkImage.as_view())
]
