from django.urls import path
from xplrmain.views import ShowFeedView, CreatePostView
from xplrmain import views

app_name = 'xplrmain'

urlpatterns = [
    path('', ShowFeedView.as_view(), name="feed-page"),
    path('interaction/follow/', views.follow, name="follow-interaction"),
    path('newpost/', CreatePostView.as_view(), name="newpost-page")
]
