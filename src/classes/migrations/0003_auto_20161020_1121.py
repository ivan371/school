# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20161020_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='pupils',
            field=models.ManyToManyField(related_name='students', to='users.Users'),
        ),
    ]
