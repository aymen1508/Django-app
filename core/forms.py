from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-3 px-4 rounded-xl',
        'placeholder': 'Username'
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'w-full py-3 px-4 rounded-xl',
        'placeholder': 'example@xxx.com'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-3 px-4 rounded-xl',
        'placeholder': 'Password'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-3 px-4 rounded-xl',
        'placeholder': 'Confirm password'
        }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-3 px-4 rounded-xl',
        'placeholder': 'Username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-3 px-4 rounded-xl',
        'placeholder': 'Password'
        }))