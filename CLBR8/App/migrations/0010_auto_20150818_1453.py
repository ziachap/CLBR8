# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_listing_hidden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('r1', models.ForeignKey(related_name='r1', to='App.Profile', null=True)),
                ('r2', models.ForeignKey(related_name='r2', to='App.Profile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'', max_length=2000)),
                ('receiver', models.ForeignKey(related_name='receiver', to='App.Profile', null=True)),
                ('sender', models.ForeignKey(related_name='sender', to='App.Profile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='listing',
            name='genre',
            field=models.CharField(max_length=64, null=True, choices=[(b'Pop', b'Pop'), (b'Reggae', b'Reggae'), (b'Folk', b'Folk'), (b'R&B/Soul', b'R&B/Soul'), (b'Jazz', b'Jazz'), (b'Indie', b'Indie'), (b'Metal', b'Metal'), (b'Rock', b'Rock'), (b'Garage', b'Garage'), (b'Drum & Bass', b'Drum & Bass'), (b'House', b'House'), (b'Hip Hop', b'Hip Hop'), (b'Dubstep', b'Dubstep'), (b'Grime', b'Grime')]),
            preserve_default=True,
        ),
    ]
