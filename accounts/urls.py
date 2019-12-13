from django.urls import path
from accounts.views import SignUpView, WelcomeView

app_name = "accounts"

urlpatterns = [
    path('signup', SignUpView.as_view(), name="sign-up-page"),
    path('welcome', WelcomeView.as_view(), name="welcome-page")
]
