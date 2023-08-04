from django import forms


class AuthorizationForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
