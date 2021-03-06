from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$', MessageList.as_view(), name="message"),
    url(r'^(?P<pk>\d+)/$', Dialogs.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/create/$', createmessage, name="create"),
    url(r'^(?P<pk>\d+)/form_message/$', FormMessage.as_view(), name="form_message")
]