# from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

from accounts.models import UserProfile
from xplrmain.models import UserPost

from api.serializers import UserProfileSerializer
from api.serializers import UserPostSerializer

class UserProfileList(APIView):
    def get(self, request):
        user_profiles = UserProfile.objects.all()[:20]
        data = UserProfileSerializer(user_profiles, many=True).data
        return Response(data)

class UserPostList(APIView):
    def get(self, request):
        user_posts = UserPost.objects.all()[:20]
        data = UserPostSerializer(user_posts, many=True).data
        return Response(data)
