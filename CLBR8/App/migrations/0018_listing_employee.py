# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_auto_20150818_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='employee',
            field=models.ForeignKey(to='App.Profile', null=True),
            preserve_default=True,
        ),
    ]
