from images.serializers import ImageCategorySerializer
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ImageCategory, Image
from rest_framework import (
    test
)
from django.urls import reverse
# Create your tests here.

class UserRegistrationAndImageCategoryTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='kalyfacloud@gmail.com',
            username='kalyfa',
            password='secret'
        )
        user = get_user_model().objects.get(pk=1)
        self.category = ImageCategory.objects.create(
            user = user,
            name = 'Animal Pictures',
            description = 'Animal Pictures'
        )

    def test_user_creation(self):
        user = get_user_model().objects.get(pk=1)
        self.assertEqual('kalyfacloud@gmail.com', user.email)
        self.assertEqual('kalyfa', user.username)
        self.assertFalse(user.is_superuser)


    def test_category_creation(self):
        user = get_user_model().objects.get(pk=1)
        image_cat = ImageCategory.objects.get(pk=1)
        self.assertEqual('Animal Pictures', image_cat.name)
        self.assertEqual('Animal Pictures', image_cat.description)
        self.assertEqual('kalyfacloud@gmail.com', user.email)

    def test_image_category_get_endpoint(self):
        client = test.APIClient()
        client.login(username='kalyfacloud@gmail.com', password='secret')
        response = client.get(
            reverse('image-category')
        )
        image_category = ImageCategory.objects.all()
        serializer = ImageCategorySerializer(image_category, many=True)
        # self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, 200)