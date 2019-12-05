from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your models here.
class UserPost(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)  # Many to One relationship
    username = models.CharField(max_length=100, default="default_username", null=True)
    go = models.ManyToManyField('UserGoPost')
    visited = models.ManyToManyField('UserVisitedPost')
    saved = models.ManyToManyField('UserSavedPost')

    def get_go_users(self):
        pass

    def get_visited_users(self):
        pass

    def get_saved_users(self):
        pass

    # picture = models.ImageField(max_length=500, default="", null=True)

    # Might want to change these to something else. Difficulty is just choosing from 3/4 available
    # premade values...
    coordinates = models.CharField(max_length=500, default="0, 0", null=True)  # Stores coordinates in comma delimeted tuple
    difficulty = models.CharField(max_length=500, default="Low", null=True)  # Defines difficulty as string

    description = models.CharField(max_length=500, default="", null=True)
    time_to_go = models.CharField(max_length=500, default="Any Time", null=True)
    verified = models.BooleanField(max_length=100, default=False, null=True)

class UserGoPost(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, default=1, on_delete=models.CASCADE)

class UserVisitedPost(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, default=1, on_delete=models.CASCADE)

class UserSavedPost(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, default=1, on_delete=models.CASCADE)
