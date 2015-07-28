# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import App.custom_models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0013_listing_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('rating_1', App.custom_models.IntegerRangeField(default=3)),
                ('rating_2', App.custom_models.IntegerRangeField(default=3)),
                ('rating_3', App.custom_models.IntegerRangeField(default=3)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
