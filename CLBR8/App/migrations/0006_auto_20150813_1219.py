# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20150813_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
