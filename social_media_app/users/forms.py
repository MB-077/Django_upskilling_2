from django import forms
from django.contrib.auth.models import User
from .models import *

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo',]
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',]
    
    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password2']
    