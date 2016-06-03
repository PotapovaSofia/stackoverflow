# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 14:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20160321_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-create_date',), 'verbose_name': '\u0421\u043e\u0431\u044b\u0442\u0438\u0435', 'verbose_name_plural': '\u0421\u043e\u0431\u044b\u0442\u0438\u044f'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='created_at',
        ),
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
        migrations.AddField(
            model_name='event',
            name='change_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='event',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='text',
            field=models.TextField(blank=True, verbose_name='\u041f\u043e\u043b\u0435 \u0432\u0432\u043e\u0434\u0430 \u0442\u0435\u043a\u0441\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
