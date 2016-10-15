from __future__ import unicode_literals
from users.models import Users
from django.db import models


class message(models.Model):
    text = models.TextField()
    time = models.TimeField()
    setter = models.ForeignKey(Users, related_name="setter")
    getter = models.ForeignKey(Users, related_name="getter")