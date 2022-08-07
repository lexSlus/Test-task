from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLogInForm(AuthenticationForm):
    username = forms.CharField(label='Имя Пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))





