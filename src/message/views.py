from django.shortcuts import render, get_object_or_404, reverse, HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView
from .models import message
from .models import User
from django import forms


class MessageList(CreateView):
    template_name = 'message/list_message.html'
    context_object_name = 'list_message'
    model = message
    fields = ['text', 'getter']

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.User_s = User.objects.filter(setter=request.user.id)
        self.User_g = User.objects.exclude(setter=request.user.id)
        print(self.User_s)
        print(self.User_g)
        return super(MessageList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MessageList, self).get_context_data(**kwargs)
        context['User_s'] = self.User_s
        context['User_g'] = self.User_g
        return context

    def form_valid(self, form):
        form.instance.setter = self.request.user
        return super(MessageList, self).form_valid(form)

    def get_success_url(self):
        return reverse('message:message')