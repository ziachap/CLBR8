from django.db import models
from App.custom_models import *
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    artist_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    producer = models.BooleanField(default=True)
    vocalist = models.BooleanField(default=False)
    fb_link = models.URLField(max_length=500, null=True, blank=True)
    tw_link = models.URLField(max_length=500, null=True, blank=True)
    sc_link = models.URLField(max_length=500, null=True, blank=True)
    yt_link = models.URLField(max_length=500, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField(max_length=8, default=0)
    description = models.TextField(max_length=2000, null=True)
    audio_file = models.FileField(upload_to='audio_files/', null=True)
    longitude = models.DecimalField(decimal_places=32, max_digits=36, default=-0.1275)
    latitude = models.DecimalField(decimal_places=32, max_digits=36, default=51.5072)

class Review(models.Model):
    owner = models.ForeignKey(User, null=True)
    summary = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    rating_1 = IntegerRangeField(min_value=1, max_value=5, default=3)
    rating_2 = IntegerRangeField(min_value=1, max_value=5, default=3)
    rating_3 = IntegerRangeField(min_value=1, max_value=5, default=3)