# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20150614_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='total_price',
        ),
    ]
