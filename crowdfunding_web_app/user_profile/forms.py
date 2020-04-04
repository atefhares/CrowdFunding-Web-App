from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile
from django.forms import ModelForm

class UserUpdateForm (forms.ModelForm):
    def __int__(self, *args, disabled_email=True, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].disabled = disabled_email

    class Meta:
        model = User
        fields =['first_name','email','last_name','first_name']

class ProfileUpdateForm (forms.ModelForm):


    class Meta:
        model = UserProfile
        fields =['phone_number','birth_date','facebook_profile_id','country','profile_pic']

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []

class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = []