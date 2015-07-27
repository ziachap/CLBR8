from App.models import Profile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('artist_name', 'profile_pic', 'bio')
