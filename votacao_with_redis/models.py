# coding: utf-8
from django.db import models


class Poll(models.Model):
    title = models.CharField('Título', max_length=55)

    class Meta:
            verbose_name = "poll"
            verbose_name_plural = "polls"

    def __str__(self):
        return self.title


class Option(models.Model):
    name = models.CharField('Opção', max_length=55)
    pool_id = models.ForeignKey(Poll)
    count = models.IntegerField()

    class Meta:
        verbose_name = "option"
        verbose_name_plural = "options"

    def __str__(self):
        return self.name
