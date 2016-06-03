# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="blog_detail"),
	#url(r'^$', BlogView.as_view(), name="blog_detail"),
]
