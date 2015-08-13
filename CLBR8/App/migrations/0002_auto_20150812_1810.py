# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_pic',
            field=stdimage.models.StdImageField(null=True, upload_to=b'listing_pictures/', blank=True),
            preserve_default=True,
        ),
    ]
