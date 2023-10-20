from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')


    class Meta:
        model = User
        fields =['username','email']
        label ={'username':'USERNAME'}






