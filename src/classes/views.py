from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import *


class ClassList(ListView):
    template_name = 'classes/list_classes.html'
    model = classes

    def get_queryset(self):
        return classes.objects.filter(teacher=self.request.user)

