from django.conf.urls import url
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name="logout"),
    url(r'^base/', login, {'template_name': 'core/main_page.html'}, name="base"),
]