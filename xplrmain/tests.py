from django.test import TestCase
from xplrmain.models import UserPost
from django.contrib.auth.models import User

# Create your tests here.

class XplrmainNewpostTest(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_new_post_saves(self):
        user = User()
        user.save()

        user_post = UserPost(
            user=user,
            username="APNovichkov",
            coordinates="123, 234",
            difficulty="Low",
            description="Cool spot bro",
            time_to_go="Never",
            verified=False)

        user_post.save()

        get_user_post = UserPost.objects.get(user=user)

        self.assertEqual(get_user_post.username, "APNovichkov")
