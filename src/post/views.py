from django.shortcuts import HttpResponse, HttpResponseRedirect, reverse, render
from django.views.generic import DetailView
from django.views.generic import ListView, CreateView
from .models import post


class PostsList(CreateView):
    template_name = 'post/list_posts.html'
    context_object_name = 'post'
    model = post
    fields = ['title', 'content', 'avatar',]

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.posts = post.objects.all()
        return super(PostsList, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(PostsList, self).get_context_data(**kwargs)
        context['posts'] = self.posts
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostsList, self).form_valid(form)

    def get_success_url(self):
        return reverse('post:post')
