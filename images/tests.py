from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ImageCategory, Image
# Create your tests here.

class UserRegistrationAndImageCategoryTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='kalyfacloud@gmail.com',
            username='kalyfa',
            password='string1234'
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