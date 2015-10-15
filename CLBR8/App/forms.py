from App.models import *
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
        fields = ('artist_name', 'bio', 'web_link', 'fb_link', 'tw_link', 'sc_link', 'yt_link', 'profile_pic')

class ListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        self.fields['price'].required = False
    class Meta:
        model = Listing
        fields = ('title', 'price', 'description', 'genre', 'listing_pic', 'audio_file', 'address', 'longitude', 'latitude')

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('description',)

class EditListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'price', 'description', 'genre', 'audio_file', 'address', 'longitude', 'latitude')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('summary', 'description', 'rating_1', 'rating_2', 'rating_3')