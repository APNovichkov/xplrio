from django.urls import path
from xplrmain.views import ShowFeedView

urlpatterns = [
    path('', ShowFeedView.as_view(), name="feed-page")
]
