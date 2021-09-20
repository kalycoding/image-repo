from django.conf.urls import url
from django.urls import path
from .views import (
    ImageCategoryViewList,
    ImageCategoryUpdateView,
    ImageListView,
    DeleteAllImagesInCategory,
    ImageVies
)

urlpatterns = [
    path('', ImageCategoryViewList.as_view(), name='image-category'),
    path('<int:pk>/images/', ImageListView.as_view(), name='image-cat-list'),
    path('<int:pk>/', ImageCategoryUpdateView.as_view(), name='image-category-update'),
    path('<int:pk>/delete/all/images/', DeleteAllImagesInCategory.as_view(), name='image-category-update')
]
