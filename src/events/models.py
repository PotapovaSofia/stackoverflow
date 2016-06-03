# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from comments.models import Comment
from like.models import Like
from django.contrib.contenttypes.fields import GenericRelation
from like.models import LikeMixin

#@python_2_unicode_compatible




class Tag(models.Model):
     name = models.CharField(max_length=255)

     def __str__(self):
         return self.name

     class Meta:
         verbose_name = u'Тэг'
         verbose_name_plural = u'Тэги'
         ordering = ('name', )  



class EventQuerySet(models.QuerySet):

    def for_user(self, user):
        if user.is_authenticated():
            queryset = self.filter(models.Q(author=user) | models.Q(is_published=True))
        else:
            queryset = self.filter(is_published=True)
        return queryset


class Event(LikeMixin):

    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    text = models.TextField(verbose_name=u'Поле ввода текста', blank=True)
    create_date = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True,  blank=True, null=True)
    #pub_date = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True,  blank=True, null=True)
    change_date = models.DateTimeField(verbose_name=u'Дата последнего редактирования', auto_now=True,  blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор', null=True)
    blog = models.ForeignKey('blog.Blog', verbose_name=u'Блог', related_name='event', blank=True, null=True)
    total = models.FloatField(default=0)
    #comments_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    #participants_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tags')
    #likes = GenericRelation(Like, content_type_field='item_type', object_id_field='i')

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'
        ordering = ('-create_date', )    
    
    def __unicode__(self):
    	return self.title

    objects = EventQuerySet.as_manager()

    def get_cent_answers_channel_name(self):
        return "event_%d"%self.id


@receiver(models.signals.post_save, sender=Comment)
def on_answer_creation(sender, instance, *args, **kwargs):
    if kwargs.get('created'):
        comment = instance
        from .tasks import send_email_notification
        send_email_notification.delay(
            'sofiapotapova95@mail.ru',
            'New answer to question "{}"'.format(comment.event.title),
            'You got answer with the text: "{}"'.format(comment.text)
        )
