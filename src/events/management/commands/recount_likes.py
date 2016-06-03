# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
#from django.contrib.auth.models import User
#from .models import Event

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
        """
        print "ololol"
