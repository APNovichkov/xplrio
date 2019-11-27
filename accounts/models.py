from django.db import models
from django.contrib.auth.models import User

# FormWizard


# Create your models here.
class UserProfile(User):
    """Model that builds on Django's User Model."""

    photography_type = models.CharField(max_length=500, default="", null=True)
    risk_level = models.CharField(max_length=500, default="", null=True)
    profile_pic = models.ImageField(max_length=500, default="", null=True)
    recent_ip = models.GenericIPAddressField(max_length=500, default="27.0.0.0", null=True)
#    interest = models.Empty()
#    user_posts = models.Empty()
#    followers = models.Empty()
#    following = models.Empty()
#    saved_posts = models.Empty()
#    visited_posts = models.Empty()

# class Graph(models.Model):
    # id = models.FloatField()
#    pass
