from __future__ import unicode_literals
from django.db import models
from users.models import Users


class like(models.Model):
    author = models.ForeignKey(Users)
