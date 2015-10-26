# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votacao_with_redis', '0002_auto_20151026_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='pool_id',
            new_name='pool',
        ),
    ]
