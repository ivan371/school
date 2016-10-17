from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import post


class PostsList(ListView):
    template_name = 'post/list_posts.html'
    context_object_name = 'post'
    model = post


