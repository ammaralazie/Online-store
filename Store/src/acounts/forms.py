from django import forms
from django.contrib.auth.models import User
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['image','country','address']

class ChangePssword(forms.ModelForm):
    class Meta:
        model=User
        fields=['password']
