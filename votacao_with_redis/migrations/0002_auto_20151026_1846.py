# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacao_with_redis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='count',
        ),
        migrations.AddField(
            model_name='option',
            name='votes',
            field=models.IntegerField(default=0, verbose_name=b'Total de votos'),
            preserve_default=False,
        ),
    ]
