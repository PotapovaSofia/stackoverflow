from django.conf.urls import url
from django.contrib.auth.decorators import login_required
import views
from .views import *

urlpatterns = [
	url(r'^(?P<content_type_id>\d+)/(?P<pk>\d+)/like/$', login_required(views.LikeView.as_view()), name='do_like'),
]