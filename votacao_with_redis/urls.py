# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/vote$', views.DetailPost.as_view(), name='vote'),
    url(r'^(?P<id>[0-9]+)/resultado$', views.DetailPost.as_view(), name='vote'),
]
