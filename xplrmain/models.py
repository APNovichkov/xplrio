from django.db import models
from accounts.models import UserProfile

# Create your models here.
class UserPost(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Many to One relationship
    go = models.ManyToManyField('UserGoPost')
    visited = models.ManyToManyField('UserVisitedPost')
    saved = models.ManyToManyField('UserSavedPost')

    # Might want to change these to something else. Difficulty is just choosing from 3/4 available
    # premade values...
    coordinates = models.CharField(max_length=500, default="0, 0", null=True)  # Stores coordinates in comma delimeted tuple
    difficulty = models.CharField(max_length=500, default="Low", null=True)  # Defines difficulty as string

    description = models.CharField(max_length=500, default="", null=True)
    time_to_go = models.CharField(max_length=500, default="Any Time", null=True)
    verified = models.BooleanField(max_length=100, default=False, null=True)

class UserGoPost(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(UserPost, on_delete=models.CASCADE)

class UserVisitedPost(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(UserPost, on_delete=models.CASCADE)

class UserSavedPost(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(UserPost, on_delete=models.CASCADE)
