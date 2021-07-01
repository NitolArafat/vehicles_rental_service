from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    phone = models.CharField(max_length=30,blank=True,null=True,unique=True)
    address = models.CharField(max_length=300,blank=True,null=True)
    image = models.ImageField(upload_to='photo/user/%y/%m/%d',blank=True,null=True)

