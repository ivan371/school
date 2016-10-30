from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    proffession = models.IntegerField(default=0)

    def __unicode__(self):
        return u'{} {} {} {} {}'.format(self.first_name, self.last_name,  self.email, self.rating, self.avatar)

    def get_messages(self):
        return self.messages
