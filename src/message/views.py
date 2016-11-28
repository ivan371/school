# coding=utf-8
#utf-8
from django.shortcuts import render, get_object_or_404, reverse, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import DetailView, CreateView, ListView, UpdateView,View
from .models import Message
from .models import Dialog
from .models import User
from django import forms
from django.http import JsonResponse


class MessageList(CreateView):
    template_name = 'message/list_message.html'
    model = Message
    fields = ['text']

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.dialog = Dialog.objects.all()
        return super(MessageList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MessageList, self).get_context_data(**kwargs)
        context['list_message'] = self.dialog
        return context

    def get_success_url(self):
        return reverse('message:message')


class FormMessage(DetailView):
    model = Dialog
    template_name = 'message/form_message.html'


class MessageForm(forms.Form):
    text = forms.CharField(max_length=255)


def createmessage(request, pk):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        print("I AM HERE")
        if form.is_valid():
            print("I AM HERE!")
            data = form.cleaned_data
            print(request)
            m = Message(
                text=data['text'],
                dial=Dialog.objects.get(id=pk),
                author=request.user,
            )
            m.save()
            return HttpResponse('Сообщение отправлено!')
    return HttpResponse('Ошибка при отправке сообщения')


class Dialogs(DetailView):
    template_name = 'message/dialog.html'
    model = Dialog


class NewMessage(CreateView):
    template_name = 'message/list_message.html'
    model = Message
    fields = ['text', 'author']

    def form_valid(self, form):
        return super(NewMessage, self).form_valid(form)


class AjaxableResponseMixin(object):
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class MessageCreate(AjaxableResponseMixin, CreateView):
    model = Message
    fields = ['text']