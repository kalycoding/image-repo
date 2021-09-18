from django.urls import path
from .views import SingleImageUploadView, BulkImageUpload

urlpatterns = [
    path('', SingleImageUploadView.as_view(), name='image-upload'),
    path('bulk/', BulkImageUpload.as_view())
    
]
