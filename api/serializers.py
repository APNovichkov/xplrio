from rest_framework.serializers import ModelSerializer

from accounts.models import UserProfile
from xplrmain.models import UserPost

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserPostSerializer(ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__'
