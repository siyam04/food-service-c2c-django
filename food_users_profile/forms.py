from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Select, Textarea
# Same App importing
from .models import *


class SignUpForm(UserCreationForm):
    """User Signup Form Creating"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    """Profile Creating Form """
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'user_name': TextInput(attrs={'class':'form-control'}),
            'email': TextInput(attrs={'class':'form-control'}),
            'contact_no': TextInput(attrs={'class':'form-control'}),
            'role': Select(attrs={'class':'form-control'}),
            'area': Select(attrs={'class':'form-control'}),
        }


