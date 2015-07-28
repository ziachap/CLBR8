# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_auto_20150728_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=0, max_length=8),
            preserve_default=True,
        ),
    ]
