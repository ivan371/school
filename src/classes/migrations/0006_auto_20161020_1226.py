# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20161020_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='pupils',
            field=models.ManyToManyField(blank=True, related_name='students', to='users.User'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='users.User'),
        ),
        migrations.AlterField(
            model_name='test',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
