from __future__ import unicode_literals
from django.db import models
from users.models import Users
from post.models import post


class like(models.Model):
    author = models.ForeignKey(Users)
    post = models.ForeignKey(post)

    def __unicode__(self):
        return u'{} {}'.format(self.author.name, self.post.title)
