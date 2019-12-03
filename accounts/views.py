from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import UserProfile

from accounts.forms import UserProfileForm


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class WelcomeView(CreateView):
    def get(self, request):
        context = {'form': UserProfileForm}
        return render(request, 'registration/welcome.html', context)

    def post(self, request):
        form = UserProfileForm(request.POST)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return HttpResponseRedirect(reverse_lazy('feed-page'))

        return render(request, 'registration/welcome.html', {'form': form})
