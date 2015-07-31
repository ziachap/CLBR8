# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(max_length=2000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='latitude',
            field=models.DecimalField(default=51.5072, max_digits=20, decimal_places=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='longitude',
            field=models.DecimalField(default=-0.1275, max_digits=20, decimal_places=16),
            preserve_default=True,
        ),
    ]
