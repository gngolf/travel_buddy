from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^logout$', views.logout),
    url(r'^welcome$', views.welcome),
    url(r'^info/(?P<id>\d+)$', views.info),

]