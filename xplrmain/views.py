from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect
# from django.utils import timezone

from django.contrib.auth.models import User
from xplrmain.models import UserPost
from xplrmain.forms import UserPostForm

# Create your views here.

class ShowFeedView(View):
    def get(self, request):
        """Return list of All(for now) UserPosts."""

        posts = UserPost.objects.all()

        context = {
            'posts': posts
        }

        return render(request, 'xplrmain/feed.html', context)

    def post(self, request):
        pass

class CreatePostView(View):
    def get(self, request):
        context = {'form': UserPostForm}
        return render(request, 'xplrmain/newpost.html', context)

    def post(self, request):
        form = UserPostForm(request.POST)

        if form.is_valid():
            print("Form is valid")
            user_post = form.save(commit=False)
            user_post.user = request.user
            #user_post.go.set(None)
            #user_post.visited = None
            #user_post.saved = None
            user_post.save()
            return HttpResponseRedirect(reverse_lazy('feed-page'))

        return render(request, 'xplrmain/newpost.html', {'form': form})
