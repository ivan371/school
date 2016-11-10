from __future__ import unicode_literals
from users.models import User
from django.db import models


class Dialog(models.Model):
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=100)


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User)
    dial = models.ForeignKey(Dialog)

