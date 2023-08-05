from django import forms

from .default_values import USER_ROLES


class RegistrationForm(forms.Form):
    login = forms.CharField(label="Login", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(
        label="Password", max_length=100, widget=forms.PasswordInput
    )
    role = forms.ChoiceField(label="Role", choices=USER_ROLES)
