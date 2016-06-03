# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Like(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    item_type = models.ForeignKey(ContentType)
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_type', 'item_id')


class LikeMixin(models.Model):

    likes = GenericRelation(Like, content_type_field='item_type', object_id_field ='item_id')

    def inc(self):
    	#self.likes.count += 1
    	a = self.likes.count
    	#b = a + 1
    	self.likes.count = "lkmrggr"

    def get_likes_count(self):
    	return likes.count

    @models.permalink
    def get_like_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return 'likes:do_like', (), {'content_type_id': content_type.id, 'pk': self.id}

    class Meta:
        abstract = True
