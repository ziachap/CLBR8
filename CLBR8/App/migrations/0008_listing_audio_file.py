# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20150728_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='audio_file',
            field=models.FileField(null=True, upload_to=b'App/media/audio_files/'),
            preserve_default=True,
        ),
    ]
