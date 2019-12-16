from django.urls import path
from xplrmain.views import ShowFeedView, CreatePostView
from xplrmain import views

app_name = 'xplrmain'

urlpatterns = [
    path('', views.redirect_from_home, name="redirect-from-home"),
    path('feed/', ShowFeedView.as_view(), name="feed-page"),
    path('interaction/follow/', views.follow, name="follow-interaction"),
    path('interaction/go', views.go, name='go-interaction'),
    path('interaction/visited', views.visited, name='visited-interaction'),
    path('interaction/save', views.save, name='save-interaction'),
    path('newpost/', CreatePostView.as_view(), name="newpost-page")
]
