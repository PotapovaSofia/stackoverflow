# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):
    pub_date = models.DateTimeField(verbose_name=u'Дата публикации', auto_now_add=True)
    title = models.CharField(verbose_name=u'Заголовок', max_length=140)

    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'
        ordering = ('-pub_date',)

    
