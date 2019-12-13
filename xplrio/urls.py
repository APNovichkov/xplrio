"""xplrio URL Configuration."""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Serializers
    path('api/', include('api.urls')),

    # xplrio App
    path('', include('xplrmain.urls')),
    path('', include('accounts.urls')),

    # Authorization
    path('', include('django.contrib.auth.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
