# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
            preserve_default=False,
        ),
    ]
