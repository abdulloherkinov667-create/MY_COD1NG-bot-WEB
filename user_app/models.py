from django.db import models
from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username