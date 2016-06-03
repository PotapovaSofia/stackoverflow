from django.conf.urls import url

from .views import *
#import views
#app_name = "events"
urlpatterns = [
    url(r'^$', name="search"),
    #
    #url(r'^categories/(?P<pk>\d+)/$', views.TagDetail.as_view(), name='tag_detail'),
]