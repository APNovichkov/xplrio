from django.shortcuts import render
from django.views import View
# from django.http import HttpResponseRedirect
# from django.utils import timezone

# Create your views here.

class ShowFeedView(View):
    def get(self, request):
        print("I am in get function")
        return render(request, 'xplrmain/feed.html', {})

    def post(self, request):
        pass
