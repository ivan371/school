from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$', PostsList.as_view(), name="post"),
    url(r'^(?P<pk>\d+)/$', PostsList.as_view(), {'foo': 'bar'}, name="detail"),
]