# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='blog',
        ),
    ]
