# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import App.custom_models
import stdimage.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0, max_length=8)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('genre', models.CharField(max_length=64, null=True, choices=[(b'Pop', b'Pop'), (b'Reggae', b'Reggae'), (b'Folk', b'Folk'), (b'R&B/Soul', b'R&B/Soul'), (b'Jazz', b'Jazz'), (b'Indie', b'Indie'), (b'Metal', b'Metal'), (b'Rock', b'Rock'), (b'Garage', b'Garage'), (b'Drum & Bass', b'Drum & Bass'), (b'House', b'House'), (b'Hip Hop', b'Hip Hop'), (b'Grime', b'Grime')])),
                ('producer', models.BooleanField(default=True)),
                ('vocalist', models.BooleanField(default=True)),
                ('audio_file', models.FileField(null=True, upload_to=b'audio_files/')),
                ('listing_pic', models.ImageField(null=True, upload_to=b'listing_pictures/', blank=True)),
                ('longitude', models.DecimalField(default=-0.1275, max_digits=36, decimal_places=32)),
                ('latitude', models.DecimalField(default=51.5072, max_digits=36, decimal_places=32)),
                ('address', models.CharField(default=b'Who knows where!', max_length=200)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('listing', models.ForeignKey(related_name='listing', to='App.Listing', null=True)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('artist_name', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=1000, null=True, blank=True)),
                ('producer', models.BooleanField(default=True)),
                ('vocalist', models.BooleanField(default=False)),
                ('fb_link', models.URLField(max_length=500, null=True, blank=True)),
                ('tw_link', models.URLField(max_length=500, null=True, blank=True)),
                ('sc_link', models.URLField(max_length=500, null=True, blank=True)),
                ('yt_link', models.URLField(max_length=500, null=True, blank=True)),
                ('profile_pic', stdimage.models.StdImageField(null=True, upload_to=b'profile_pictures/', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('rating_1', App.custom_models.IntegerRangeField(default=3)),
                ('rating_2', App.custom_models.IntegerRangeField(default=3)),
                ('rating_3', App.custom_models.IntegerRangeField(default=3)),
                ('author', models.ForeignKey(related_name='author', to='App.Profile', null=True)),
                ('recipient', models.ForeignKey(related_name='recipient', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
