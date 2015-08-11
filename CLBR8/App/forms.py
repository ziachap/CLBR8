from App.models import Profile, Listing
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('artist_name', 'producer', 'vocalist', 'profile_pic')

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('artist_name', 'bio', 'fb_link', 'tw_link', 'sc_link', 'yt_link', 'profile_pic')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'price', 'description', 'genre', 'audio_file', 'address', 'longitude', 'latitude')

class EditListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'price', 'description', 'genre', 'audio_file', 'address', 'longitude', 'latitude')
