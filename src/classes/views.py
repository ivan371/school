from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import *


class ClassList(ListView):
    template_name = 'post/list_classes.html'
    context_object_name = 'class'
    newclass = classes.objects.all()
    claz = []
    for cl in newclass:
        claz.append(pupils.objects.filter(clas=cl))
    model = claz


