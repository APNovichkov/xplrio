from django.db import models


# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=50, unique=True)
    profile_pic = models.ImageField()
    recent_ip = models.GenericIPAddressField()
