# coding: utf-8
import random
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Poll, Option

import redis
cache = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


@never_cache
def incluir_voto_mysql(request):
    options = [1, 2, 3, 4]
    result = random.choice(options)
    option = Option.objects.filter(id=result)[0]
    option.votes += 1
    option.save()

    context = {'text': 'Seu voto foi realizado com sucesso no MySQL'}

    return render(request, 'votacao_with_redis/voto_ok.html', context)


@never_cache
def incluir_voto_redis(request):
    options = [1, 2, 3, 4]
    result = random.choice(options)
    cache.incr('votacao:option:{}'.format(result))

    context = {'text': 'Seu voto foi realizado com sucesso no REDIS'}

    return render(request, 'votacao_with_redis/voto_ok.html', context)
