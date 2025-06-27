from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class UserConfig(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, related_name="config"
    )
    languague = models.CharField(
        max_length=255, choices=[("en", "English"), ("es", "Spanish")], default="es"
    )
    theme = models.CharField(
        max_length=255, choices=[("light", "Light"), ("dark", "Dark")], default="light"
    )
