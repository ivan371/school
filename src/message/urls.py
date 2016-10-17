from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$', MessageList.as_view(), name="message"),
]