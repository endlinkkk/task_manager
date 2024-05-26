from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BootstrapRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput({"class": "form-control", "placeholder": "User name"}),
    )
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(
            {"class": "form-control", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(
            {"class": "form-control", "placeholder": "Password"}
        ),
    )


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput({"class": "form-control", "placeholder": "User name"}),
    )
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(
            {"class": "form-control", "placeholder": "Password"}
        ),
    )
