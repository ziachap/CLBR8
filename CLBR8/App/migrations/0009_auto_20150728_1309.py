# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_listing_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='audio_file',
            field=models.FileField(null=True, upload_to=b'audio_files/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=b'profile_pictures/', blank=True),
            preserve_default=True,
        ),
    ]
