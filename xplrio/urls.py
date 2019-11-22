"""xplrio URL Configuration."""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # xplrio App
    path('', include('xplrmain.urls')),
    path('', include('accounts.urls')),

    # Authorization
    path('accounts/', include('django.contrib.auth.urls'))
]
