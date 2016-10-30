from __future__ import unicode_literals
from users.models import User
from django.db import models


class message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    setter = models.ForeignKey(User, related_name="setter")
    getter = models.ForeignKey(User, related_name="getter")
