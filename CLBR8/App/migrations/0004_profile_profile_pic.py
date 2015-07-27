# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20150724_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to=b'static/images/profile_pictures/', null=True, verbose_name=b'profile picture', blank=True),
            preserve_default=True,
        ),
    ]
