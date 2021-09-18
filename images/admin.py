from re import I
from django.contrib import admin
from .models import (
    ImageCategory,
    Image
)
# Register your models here.

admin.site.register(Image)
admin.site.register(ImageCategory)