from django.contrib.auth.models import User
from .models import Profile
from django.test import TestCase


class UserProfileCountTest(TestCase):
    def test_user_profile_count(self):
        user_count = User.objects.count()
        profile_count = Profile.objects.count()
        self.assertEqual(user_count, profile_count)
