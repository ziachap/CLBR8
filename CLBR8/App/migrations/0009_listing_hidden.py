# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20150817_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='hidden',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
