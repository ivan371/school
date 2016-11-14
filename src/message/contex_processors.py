from django.shortcuts import render, get_object_or_404, reverse, HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView
from .models import Message
from .models import Dialog
from .models import User
from django import forms
from django.db import models


class MyForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('author', 'dial')


def messages(request):
    form = MyForm(request.POST or None)
    if request.method == 'POST':
            if form.is_valid():
                m = form.save(commit=False)
                print(m)
                m.author = request.user
                m.dial = Dialog.objects.get(id=request.POST['dial'])
                m.save()
    return {'list_message': Dialog.objects.all(), 'newform': form}