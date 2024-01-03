from django.db import models

# Create your models here.
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
