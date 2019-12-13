from django.urls import path

from api.views import UserProfileList, UserPostList

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='polls_list'),
    path('posts/', UserPostList.as_view(), name='polls_detail')
]
