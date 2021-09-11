from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
# Create your models here.



class ImageCategory(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    public_image = models.BooleanField(default=True)

    
    image_category = models.ForeignKey(
        to=ImageCategory,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name