# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161017_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='sender',
            new_name='send',
        ),
    ]