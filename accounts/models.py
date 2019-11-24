from django.db import models


# Create your models here.
class user(models.Model):
    user_id = models.FloatField()  # randomly genrated byte
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    photography_type = models.CharField(max_length=20)
    risk_level = models.CharField(max_length=12)
    profile_pic = models.ImageField()
    recent_ip = models.GenericIPAddressField()
    interest = models.Empty()
    user_posts = models.Empty()
    followers = models.Empty()
    following = models.Empty()
    saved_posts = models.Empty()
    visited_posts = models.Empty()
