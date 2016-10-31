from __future__ import unicode_literals
from django.db import models
from users.models import User


class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __unicode__(self):
        return u'{} {} {}'.format(self.title, self.created_at, self.author.username)

    def count_likes(self):
        return self.likes.count()