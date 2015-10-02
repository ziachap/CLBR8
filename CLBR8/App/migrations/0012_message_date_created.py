# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_message_conversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
