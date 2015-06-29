# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_hotel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='url',
            field=models.CharField(max_length=800),
        ),
    ]
