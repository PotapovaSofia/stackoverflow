from django.conf.urls import url

from .views import *
#import views
#app_name = "events"
urlpatterns = [
    url(r'^$', EventList.as_view(), name="event_list"),
    url(r'^(?P<pk>\d+)/$', EventDetail.as_view(), name="event_detail"),
    url(r'^create/$', EventCreate.as_view(), name="event_create"),
    url(r'^(?P<pk>\d+)/update/$', EventUpdate.as_view(), name="event_update"),
    #
    #url(r'^categories/(?P<pk>\d+)/$', views.TagDetail.as_view(), name='tag_detail'),
]