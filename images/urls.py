from django.conf.urls import url
from django.urls import path
from .views import ImageCategoryViewList

urlpatterns = [
    path('', ImageCategoryViewList.as_view(), name='image-category')
]
