# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_auto_20150730_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='latitude',
            field=models.DecimalField(default=51.5072, max_digits=36, decimal_places=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='longitude',
            field=models.DecimalField(default=-0.1275, max_digits=36, decimal_places=32),
            preserve_default=True,
        ),
    ]
