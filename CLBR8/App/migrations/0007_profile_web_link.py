# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20150813_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='web_link',
            field=models.URLField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
