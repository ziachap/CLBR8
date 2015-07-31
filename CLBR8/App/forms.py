from App.models import Profile, Listing
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('artist_name', 'producer', 'vocalist', 'profile_pic')

class ListingForm(forms.ModelForm):
    #title = forms.CharField()

    class Meta:
        model = Listing
        fields = ('title', 'price', 'description', 'audio_file', 'longitude', 'latitude')

