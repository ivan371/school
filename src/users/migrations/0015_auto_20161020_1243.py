# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_user_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='proffession',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
