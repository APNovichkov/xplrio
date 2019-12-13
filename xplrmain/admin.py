from django.contrib import admin
from .models import UserPost, UserGoPost, UserVisitedPost, UserSavedPost

# Register your models here.
admin.site.register(UserPost)
admin.site.register(UserGoPost)
admin.site.register(UserVisitedPost)
admin.site.register(UserSavedPost)
