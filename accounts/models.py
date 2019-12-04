from django.db import models
from django.contrib.auth.models import User

# FormWizard


# Create your models here.
class UserProfile(models.Model):
    """Model that builds on Django's User Model."""

    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    first_name = models.CharField(default="", max_length=32, help_text='First name')
    last_name = models.CharField(default="", max_length=32, help_text='Last name')
    email = models.EmailField(default="", max_length=64, help_text='Enter a valid email address')

    photography_type = models.CharField(max_length=500, default="", null=True)
    risk_level = models.CharField(max_length=500, default="", null=True)
    profile_pic = models.ImageField(upload_to="media/profile_pics", max_length=500, default="", null=True)
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
