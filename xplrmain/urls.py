from django.urls import path
from xplrmain.views import ShowFeedView, CreatePostView

urlpatterns = [
    path('', ShowFeedView.as_view(), name="feed-page"),
    path('newpost/', CreatePostView.as_view(), name="newpost-page")
]
