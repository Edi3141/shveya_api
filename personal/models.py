from django.db import models
from account.models import CustomUser


class Personal(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_profile/', blank=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.name
