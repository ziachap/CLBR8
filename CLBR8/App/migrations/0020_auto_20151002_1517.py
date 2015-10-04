# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_auto_20150930_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='listing',
            field=models.ForeignKey(related_name='related_listing', to='App.Listing', null=True),
            preserve_default=True,
        ),
    ]
