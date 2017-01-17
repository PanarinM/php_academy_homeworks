from django import forms
from django.core.exceptions import ValidationError
from accounts.models import User


# def validate_username(value):
#     if not User.objects.filter(username=value).exists():
#         raise ValidationError("Username doesn't exist!", params={'value': value},)


# def validate_password(value):
#     if not User.check_password(value):
#         raise ValidationError("Wrong password!", params={'value': value},)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=100)
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
