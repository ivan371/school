from __future__ import unicode_literals
from django.db import models
from users.models import Users


class classes(models.Model):
    teacher = models.ForeignKey(Users, related_name="teacher")
    list_pupils = 0

    def get_pupils(self):
        self.list_pupils = pupils.objects.filter(clas=self)
        return self.list_pupils

    def count_pupils(self):
        return self.pupit_count

    def count_tests(self):
        return self.test_count

    def count_new_tests(self):
        return self.new_test_count


class pupils(models.Model):
    clas = models.ForeignKey(classes)
    pupil = models.ForeignKey(Users, related_name="pupil")


class test(models.Model):
    testclass = models.ForeignKey(classes)
    sender = models.ForeignKey(Users)
    file = models.FileField(upload_to='tests',)
    mark = models.IntegerField()