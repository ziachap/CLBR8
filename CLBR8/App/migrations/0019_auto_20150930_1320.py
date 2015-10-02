# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_listing_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='employee',
            field=models.ForeignKey(blank=True, to='App.Profile', null=True),
            preserve_default=True,
        ),
    ]
