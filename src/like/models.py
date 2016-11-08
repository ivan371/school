from __future__ import unicode_literals
from django.db import models
from users.models import User
from post.models import Post


class Like(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return u'{} {}'.format(self.author.name, self.post.title)
