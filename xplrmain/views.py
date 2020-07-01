from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect
# from django.utils import timezone


from xplrmain.models import UserPost, UserGoPost, UserVisitedPost, UserSavedPost
from accounts.models import UserProfile, UserToUserFriendship
from xplrmain.forms import UserPostForm
from django.contrib.auth.decorators import login_required


def redirect_from_home(request):
    """Redirects to login if user not authenticated, otherwise shows feed."""
    if request.user is None:
        print("Request.user is none")
    else:
        print("Request.user is not none")
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('xplrmain:feed-page'))

    return HttpResponseRedirect('login')


# @login_required(login_url="/login")
class ShowFeedView(View):
    """Shows the feed to the current user."""

    def get(self, request):
        """Return list of All(for now) UserPosts."""

        # user_profile = UserProfile.objects.get(user=request.user)
        # print("Current user profile: {} {} with user_id: {}".format(user_profile.first_name, user_profile.last_name, user_profile.user_id))

        # following = [u.friend for u in user_profile.get_following()]
        # print("Following id's: {}".format(following))

        # posts = UserPost.objects.filter(user__in=following)
        posts = UserPost.objects.all()
        # user = UserProfile.objects.get(user=request.user)

        context = {
            'posts': posts,
        #     'user': user
        }

        return render(request, 'xplrmain/feed.html', context)

    def post(self, request):
        pass

class CreatePostView(View):
    """Manages get and post requests for creating a new post."""

    def get(self, request):
        context = {'form': UserPostForm}
        return render(request, 'xplrmain/newpost.html', context)

    def post(self, request):
        form = UserPostForm(request.POST)

        if form.is_valid():
            print("Form is valid")
            user_post = form.save(commit=False)
            user_post.user = request.user
            user_post.username = request.user.username

            user_post.save()

            # user_post.go.set(request.user.id)
            # user_post.visited = None
            # user_post.saved = None

            return HttpResponseRedirect(reverse_lazy('xplrmain:feed-page'))

        return render(request, 'xplrmain/newpost.html', {'form': form})


def follow(request):
    """Manages follow functionality."""

    if request.method == 'POST':
        friendship_creator = request.user
        friend = User.objects.get(id=request.POST['post_user_id'])

        new_friendship = UserToUserFriendship(creator=friendship_creator, friend=friend)
        new_friendship.save()

        print("Saved new friendship between {} and {}".format(friendship_creator.username, friend.username))

        return HttpResponseRedirect(reverse_lazy('xplrmain:feed-page'))

def go(request):
    """Manages go functionality."""

    if request.method == 'POST':
        go_creator = request.user
        post = UserPost.objects.get(id=request.POST['post_id'])

        new_go_relationship = UserGoPost(user=go_creator, post=post)
        new_go_relationship.save()

        print("Created new go relationship between user: {} and post by user: {}".format(go_creator.username, post.username))

        return HttpResponseRedirect(reverse_lazy('xplrmain:feed-page'))

def visited(request):
    """Manages visited functionality."""

    if request.method == 'POST':
        go_creator = request.user
        post = UserPost.objects.get(id=request.POST['post_id'])

        new_visited_relationship = UserVisitedPost(user=go_creator, post=post)
        new_visited_relationship.save()

        print("Created new visited relationship between user: {} and post by user: {}".format(go_creator.username, post.username))

        return HttpResponseRedirect(reverse_lazy('xplrmain:feed-page'))

def save(request):
    """Manages save functionality."""

    if request.method == 'POST':
        go_creator = request.user
        post = UserPost.objects.get(id=request.POST['post_id'])

        new_save_relationship = UserSavedPost(user=go_creator, post=post)
        new_save_relationship.save()

        print("Created new save relationship between user: {} and post by user: {}".format(go_creator.username, post.username))

        return HttpResponseRedirect(reverse_lazy('xplrmain:feed-page'))

def unfollow(request):
    """Manages unfollow functionality."""

    if request.method == 'POST':
        friendship_creator = request.user
        friend = User.objects.get(id=request.POST['post_user_id'])

        UserToUserFriendship.get(creator=friendship_creator, friend=friend).delete()

        print("Broke friendship between {} and {}".format(friendship_creator.username, friend.username))
