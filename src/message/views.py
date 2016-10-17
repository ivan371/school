from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import message


class MessageList(ListView):
    template_name = 'message/list_message.html'
    context_object_name = 'list_message'
    model = message
