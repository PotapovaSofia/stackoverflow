# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20160427_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like_count',
        ),
    ]
