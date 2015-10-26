# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mysql/vote/$', views.incluir_voto_mysql, name='vote_mysql'),
    url(r'^redis/vote/$', views.incluir_voto_redis, name='vote_redis'),
]
