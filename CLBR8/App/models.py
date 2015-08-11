from django.db import models
from App.custom_models import *
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    date_created = models.DateField(auto_now_add=True, null=True)
    artist_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    producer = models.BooleanField(default=True)
    vocalist = models.BooleanField(default=False)
    fb_link = models.URLField(max_length=500, null=True, blank=True)
    tw_link = models.URLField(max_length=500, null=True, blank=True)
    sc_link = models.URLField(max_length=500, null=True, blank=True)
    yt_link = models.URLField(max_length=500, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    def __str__(self):
        return "%s" % self.user.username
class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField(max_length=8, default=0)
    description = models.TextField(max_length=2000, null=True)
    GENRES = (
      ('Pop', 'Pop'),
      ('Reggae', 'Reggae'),
      ('Folk', 'Folk'),
      ('R&B/Soul', 'R&B/Soul'),
      ('Jazz', 'Jazz'),
      ('Indie', 'Indie'),
      ('Metal', 'Metal'),
      ('Rock', 'Rock'),
      ('Garage', 'Garage'),
      ('Drum & Bass', 'Drum & Bass'),
      ('House', 'House'),
      ('Hip Hop', 'Hip Hop'),
      ('Grime', 'Grime'),
    )
    genre = models.CharField(max_length=64, choices=GENRES, null=True)
    producer = models.BooleanField(default=True)
    vocalist = models.BooleanField(default=True)
    audio_file = models.FileField(upload_to='audio_files/', null=True)
    listing_pic = models.ImageField(upload_to='listing_pictures/', null=True, blank=True)
    longitude = models.DecimalField(decimal_places=32, max_digits=36, default=-0.1275)
    latitude = models.DecimalField(decimal_places=32, max_digits=36, default=51.5072)
    address = models.CharField(max_length=200, default='Who knows where!')


class Review(models.Model):
    author = models.ForeignKey(Profile, null=True, related_name='author')
    recipient = models.ForeignKey(User, null=True, related_name='recipient')
    summary = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    rating_1 = IntegerRangeField(min_value=1, max_value=5, default=3)
    rating_2 = IntegerRangeField(min_value=1, max_value=5, default=3)
    rating_3 = IntegerRangeField(min_value=1, max_value=5, default=3)