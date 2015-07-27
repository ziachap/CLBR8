# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_link',
            field=models.URLField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='sc_link',
            field=models.URLField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='tw_link',
            field=models.URLField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='yt_link',
            field=models.URLField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
