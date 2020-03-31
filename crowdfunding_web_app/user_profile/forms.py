from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile

class UserUpdateForm (forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username','email','last_name','first_name']

class ProfileUpdateForm (forms.ModelForm):


    class Meta:
        model = UserProfile
        fields =['phone_number','birth_date','facebook_profile','country','profile_pic']