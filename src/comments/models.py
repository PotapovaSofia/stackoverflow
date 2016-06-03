# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from adjacent import Client
from django.dispatch import receiver
from like.models import LikeMixin
from datetime import datetime
from django.template.defaultfilters import date as _date

class Comment(LikeMixin):

    text = models.TextField(verbose_name=u'Поле ввода текста', max_length=400)
    create_date= models.DateTimeField(verbose_name=u'Дата публикации', auto_now_add=True,  blank=True, null=True)
    change_date = models.DateTimeField(verbose_name=u'Дата последнего редактирования', auto_now=True,  blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор', related_name='comments')
    event = models.ForeignKey('events.Event', verbose_name=u'Событие', related_name='comments')
    #like_count = models.IntegerField(default=0)


    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = ('-create_date', )

    def as_compact_dict(self):
        return {"author": self.author.pk, "text": self.text, "pub_date": _date(self.create_date, 'd b Y г. H:i'), "change_date": _date(self.change_date, 'd b Y г. H:i')}


#class Participant(models.Model):
@receiver(models.signals.post_save, sender=Comment)
def on_answer_creation(sender, instance, *args, **kwargs):
    if kwargs.get('created'):
        comment = instance
        client = Client()
        client.publish(comment.event.get_cent_answers_channel_name(), comment.as_compact_dict())
        response = client.send()
        print('sent to channel {}, got response from centrifugo: {}'.format(comment.event.get_cent_answers_channel_name(), response))

