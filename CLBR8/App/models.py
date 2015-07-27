from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    artist_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, null=True)
    fb_link = models.URLField(max_length=500, null=True)
    tw_link = models.URLField(max_length=500, null=True)
    sc_link = models.URLField(max_length=500, null=True)
    yt_link = models.URLField(max_length=500, null=True)
    profile_pic = models.ImageField(upload_to='App/media/profile_pictures/', null=True, blank=True)

#class Listing(models.Model):
#    title = models.CharField(max_length=100)
#    description = models.TextField(max_length=1000, null=True)