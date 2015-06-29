# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crime',
            name='datetime',
            field=models.CharField(default=datetime.datetime(2015, 6, 14, 2, 28, 57, 101454, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
