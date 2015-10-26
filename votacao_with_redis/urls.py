# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mysql/vote/$', views.incluir_voto_mysql, name='vote_mysql'),
    url(r'^redis/vote/$', views.incluir_voto_redis, name='vote_redis'),
    url(r'^mysql/resultado/$', views.resultado_mysql, name='resultado_mysql'),
    url(r'^redis/resultado/$', views.resultado_redis, name='resultado_redis'),

]
