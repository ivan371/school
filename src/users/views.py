from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Users


def home(request):
    return render(request, 'users/home.html')


class UserList(ListView):
    template_name = 'users/list_users.html'
    context_object_name = 'list_users'
    model = Users


class show_user(DetailView):
    template_name = 'users/deteled_user.html'
    context_object_name = 'us'
    model = Users
