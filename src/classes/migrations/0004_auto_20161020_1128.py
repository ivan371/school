# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20161020_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='pupils',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='users.Users'),
        ),
    ]
