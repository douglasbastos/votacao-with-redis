# coding: utf-8
import random
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Option
from django.conf import settings


import redis
cache = redis.StrictRedis(host=settings.REDIS_DB['host'],
                          port=settings.REDIS_DB['port'],
                          db=settings.REDIS_DB['db'])


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


def resultado_mysql(request):
    options = Option.objects.all().order_by('-votes')
    context = {'options': options}
    return render(request, 'votacao_with_redis/voto_ok.html', context)


def resultado_redis(request):
    option1 = cache.get('ranking:option:1')
    option2 = cache.get('ranking:option:2')
    option3 = cache.get('ranking:option:3')
    option4 = cache.get('ranking:option:4')
    context = {'votes': sorted([option1, option2, option3, option4], reverse=True)}

    return render(request, 'votacao_with_redis/voto_ok.html', context)
