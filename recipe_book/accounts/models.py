from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.CharField(max_length=254, unique=True)
    role = models.CharField(
        max_length = 10,
        choices = [('f', 'Foodie'), ('c', 'Chef')],
        default='f'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone})"

