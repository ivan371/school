# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20161020_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='proffession',
        ),
    ]
