from __future__ import unicode_literals
from django.db import models
from users.models import User


class Classes(models.Model):
    teacher = models.ForeignKey(User, related_name="teacher")
    classname = models.CharField(max_length=1000, default=0)
    pupils = models.ManyToManyField(User, related_name="students", blank=True)

    def count_pupils(self):
        return self.pupit_count

    def count_tests(self):
        return self.test_count

    def count_new_tests(self):
        return self.new_test_count


class Test(models.Model):
    testclass = models.ForeignKey(Classes)
    sender = models.ForeignKey(User)
    file = models.FileField(upload_to='tests',)
    mark = models.IntegerField()