from django.db import models
from django.contrib.auth.models import User


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

    def get_following(self):
        following = UserToUserFriendship.objects.filter(creator=self.user)
        return following

    def get_followers(self):
        followers = UserToUserFriendship.objects.filter(following=self.user)
        return followers

    # TODO
    def get_saved_posts(self):
        pass

    def get_visited_posts(self):
        pass

    def get_self_posts(self):
        pass

class UserToUserFriendship(models.Model):
    """Model to relate follow relationship between two users."""

    # Time following was made
    time_connected = models.DateTimeField(auto_now_add=True, editable=False)

    # User who is followed/created connection
    creator = models.ForeignKey(User, related_name="friendship_creator", default=1, on_delete=models.CASCADE)

    # User who "user" followed
    friend = models.ForeignKey(User, related_name="friend", default=2, on_delete=models.CASCADE)


# class Graph(models.Model):
    # id = models.FloatField()
#    pass
