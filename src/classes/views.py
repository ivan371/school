from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, reverse, get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from post.models import post
from post.forms import PostsListForm, PostForm


class ClassList(ListView):
    template_name = 'classes/list_classes.html'
    model = classes

    def get_queryset(self):
        return classes.objects.filter(teacher=self.request.user)


class PostUpdate(UpdateView):
    template_name = 'post/list_post.html'
    model = post
    context_object_name = 'class'
    fields = ('title', 'content',)

    def get_queryset(self):
        return post.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post:post')


class PostsList(CreateView):
    template_name = 'post/list_posts.html'
    context_object_name = 'post'
    model = post
    fields = ['title', 'content', 'avatar',]

    def dispatch(self, request, pk, *args, **kwargs):
        queryset = get_object_or_404(classes.objects.all(), id=pk)
        self.clasz = queryset
        self.posts = post.objects.filter(clasz=queryset)
        self.form = PostsListForm(request.GET)
        self.form.is_valid()
        if self.form.cleaned_data.get('search'):
            self.posts = self.posts.filter(title=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            self.posts = self.posts.order_by(self.form.cleaned_data['sort_field'])
        return super(PostsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostsList, self).get_context_data(**kwargs)
        context['posts'] = self.posts
        context['sform'] = self.form
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.clasz = self.clasz
        return super(PostsList, self).form_valid(form)

    def get_success_url(self):
        return reverse('classes:classes')
