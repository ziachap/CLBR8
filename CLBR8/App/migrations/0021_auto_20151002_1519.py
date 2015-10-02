# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0020_auto_20151002_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='listing',
            field=models.ForeignKey(to='App.Listing', null=True),
            preserve_default=True,
        ),
    ]
