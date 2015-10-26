# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55, verbose_name=b'Op\xc3\xa7\xc3\xa3o')),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'option',
                'verbose_name_plural': 'options',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=55, verbose_name=b'T\xc3\xadtulo')),
            ],
            options={
                'verbose_name': 'poll',
                'verbose_name_plural': 'polls',
            },
        ),
        migrations.AddField(
            model_name='option',
            name='pool_id',
            field=models.ForeignKey(to='votacao_with_redis.Poll'),
        ),
    ]
