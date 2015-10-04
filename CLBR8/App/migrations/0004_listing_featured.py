# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
