# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 11:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='getter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='getter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='setter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='setter', to=settings.AUTH_USER_MODEL),
        ),
    ]