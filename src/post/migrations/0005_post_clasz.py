# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_classes_classname'),
        ('post', '0004_auto_20161030_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='clasz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classes.classes'),
            preserve_default=False,
        ),
    ]
