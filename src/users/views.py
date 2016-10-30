from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import User


def home(request):
    return render(request, 'users/home.html')


class UserList(ListView):
    template_name = 'users/list_users.html'
    context_object_name = 'list_users'
    model = User


class show_user(DetailView):
    template_name = 'users/deteled_user.html'
    context_object_name = 'us'
    model = User


class registration(CreateView):
    template_name = 'users/registration.html'
    model = User
    fields = ['username', 'password', 'first_name', 'email', 'last_name', 'proffession', 'avatar']

    def get_success_url(self):
        return reverse('users:registration_complete')


def registration_complete(request):
    return render(request, 'users/registration_complete.html')


class self_room(ListView):
    template_name = 'users/self_room.html'
    model = User
    fields = ('last_name', 'avatar', 'first_name')


class self_update(UpdateView):
    template_name = 'users/self_update.html'
    model = User
    fields = ('last_name', 'avatar', 'first_name')

    def get_success_url(self):
        return reverse('users:self_room')

    def get_object(self, queryset=None):
        return self.request.user
