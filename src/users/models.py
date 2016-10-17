from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(models.Model):
    login = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rating = models.IntegerField()
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    proffession = models.IntegerField()

    def __unicode__(self):
        return u'{} {} {} {} {}'.format(self.login, self.name, self.surname, self.email, self.rating, self.avatar)


class claz(models.Model):
    teacher = models.ForeignKey(Users, related_name="teacher")
    pupil = models.ForeignKey(Users, related_name="pupil")


class test(models.Model):
    testclass = models.ForeignKey(claz)
    sender = models.ForeignKey(Users)
    file = models.FileField()