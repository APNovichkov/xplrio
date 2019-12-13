from django.test import TestCase

from accounts.models import UserProfile
from django.contrib.auth.models import User

# Create your tests here.
class AccountsUserProfileTest(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_user_profile_creation(self):
        user = User()
        user.save()

        user_profile = UserProfile(
            user=user,
            first_name="Andrey",
            last_name="Novichkov",
            email="andreynovichkov@gmail.com",
            photography_type="Beginner",
            risk_level="High",
            profile_pic=None,
            recent_ip="127.0.0.1")

        user_profile.save()

        get_user_profile = UserProfile.objects.get(user=user)

        self.assertEqual(get_user_profile.first_name, 'Andrey')

class AccountsTestAuthentication(TestCase):
    def test_login_page(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("username", str(response.context['form']))
