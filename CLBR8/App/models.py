from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    artist_name = models.CharField(max_length=100)
    #bio = models.TextField(max_length=1000)
    #fb_link = models.URLField(max_length=500)
    #sc_link = models.URLField(max_length=500)
    #yt_link = models.URLField(max_length=500)
    #profile_pic = (upload_to='profile_pic', blank=True)

#class Listing(models.Model):
#    title = models.CharField(max_length=100)