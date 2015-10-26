# coding: utf-8
import random
from django.shortcuts import render
from .models import Poll, Option


def incluir_voto_mysql(request):
    options = [1, 2, 3, 4]
    result = random.choice(options)
    option = Option.objects.filter(id=result)[0]

    option.votes += 1
    option.save()
    context = {'text': 'Seu voto foi realizado com sucesso'}

    return render(request, 'votacao_with_redis/voto_ok.html', context)


def incluir_voto_redis(request, **kwargs):
    pass