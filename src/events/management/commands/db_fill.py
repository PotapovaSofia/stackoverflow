# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from ...models import *
from comments.models import Comment
from blog.models import Blog


import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
    	"""
        users = list(User.objects.all())
        for i in range(100):
            q = Event()
            q.author = random.choice(users)
            q.title = u'title {}'.format(i)
            q.text = u'text {}'.format(i)
            q.is_published = True
            q.save()

        print "completed"
        """
        users = list(User.objects.all())
        b = []
        p = []
        c = []
        for _ in range(10):
            b.append(Blog.objects.create())
        for i in range(100):
            t = Event(author=random.choice(users), title = u'title {}'.format(i),
                     text = u'text {}'.format(i), is_published = True,
                     blog=random.choice(b))
            p.append(t)
            t.save()
            Tag.objects.create(name='tag{}'.format(i))
            # TODO tags.add(tag)
        for i in range(1000):
            com = Comment(author = random.choice(users), event = random.choice(p),
                           text=u'text {}'.format(i))
            c.append(com)
            com.save()
        print "completed"