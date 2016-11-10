from django.shortcuts import HttpResponse, HttpResponseRedirect, reverse, render
from django.views.generic import DetailView
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostsListForm, PostForm


class PostsList(CreateView):
    template_name = 'post/list_posts.html'
    context_object_name = 'post'
    model = Post
    fields = ['title', 'content',]

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.posts = Post.objects.all()
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
        return super(PostsList, self).form_valid(form)

    def get_success_url(self):
        return reverse('post:post')


class PostsClass(CreateView):
    template_name = 'post/list_posts.html'
    context_object_name = 'post'
    model = Post
    fields = ['title', 'content']

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.posts = Post.objects.all()
        return super(PostsClass, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostsClass, self).get_context_data(**kwargs)
        context['posts'] = self.posts
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostsClass, self).form_valid(form)

    def get_success_url(self):
        return reverse('post:post')