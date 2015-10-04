# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fb_link',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sc_link',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='yt_link',
        ),
    ]
