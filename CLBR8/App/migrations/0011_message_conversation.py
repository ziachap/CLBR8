# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20150818_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(related_name='conversation', to='App.Conversation', null=True),
            preserve_default=True,
        ),
    ]
