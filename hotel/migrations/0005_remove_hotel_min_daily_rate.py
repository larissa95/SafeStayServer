# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_remove_hotel_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='min_daily_rate',
        ),
    ]
