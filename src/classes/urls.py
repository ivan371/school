from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    url(r'^$', ClassList.as_view(), name="classes"),
    url(r'^$', ClassList.as_view(), name="classes"),
    url(r'^(?P<pk>\d+)/$', PostsList.as_view(),  {'foo': 'bar'}, name="detail"),
]
