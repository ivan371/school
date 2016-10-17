from django.conf.urls import url
from .views import *
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'users/$', UserList.as_view(), name='list_users'),
    url(r'home/$', home, name='home'),
    url(r'^(?P<pk>\d+)/$', show_user.as_view(), name="detail"),
]