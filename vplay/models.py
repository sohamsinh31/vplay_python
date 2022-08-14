from unicodedata import category
from django.db import models
from django.contrib.auth.models import User,auth

class uploads(models.Model):
    title=models.CharField(max_length=255)
    description = models.CharField(max_length=355)
    vidpath = models.CharField(max_length=255)
    thumbpath = models.CharField(max_length=255)
    uploadby = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date = models.DateTimeField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile=models.CharField(max_length=255)