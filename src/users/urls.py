from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'users/$', UserList.as_view(), name='list_users'),
    url(r'home/$', home, name='home'),
    url(r'^(?P<pk>\d+)/$', Show_user.as_view(), name="detail"),
    url(r'^login/', login, {'template_name': 'users/login.html'}, name="login"),
    url(r'^logout/', logout, {'next_page': '../home'}, name="logout"),
    url(r'^registration/', Registration.as_view(), name="registration"),
    url(r'^self_room/', Self_room.as_view(), name="self_room"),
    url(r'^self_update/', Self_update.as_view(), name="self_update"),
    url(r'^registration_complete/', registration_complete, name="registration_complete"),
]