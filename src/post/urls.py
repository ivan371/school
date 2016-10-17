from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    url(r'^post/$', PostsList.as_view(), name="post"),
]