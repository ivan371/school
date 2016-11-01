from django.conf.urls import url
from .views import *
from classes.views import PostUpdate
from django.contrib import admin

urlpatterns = [
    url(r'^$', PostsList.as_view(), name="post"),
    url(r'^(?P<pk>\d+)/$', PostUpdate.as_view(), name="detail"),
]