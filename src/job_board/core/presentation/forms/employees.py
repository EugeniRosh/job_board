from core.presentation.validators import (
    ValidateFileExtension,
    ValidatorFileSize,
    ValidatorMaxNumberValue,
)
from django import forms


class EmployeesForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, strip=True)
    surname = forms.CharField(label="Surname", max_length=50, strip=True)
    photo = forms.ImageField(
        label="Photo",
        validators=[
            ValidateFileExtension(["jpeg", "jpg", "png"]),
            ValidatorFileSize(5_000_000),
        ],
    )
    country = forms.CharField(label="Country", max_length=100, strip=True)
    city = forms.CharField(label="City", max_length=100, strip=True)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=20, strip=True)
    password = forms.CharField(label="Password", max_length=150)
    position = forms.CharField(
        label="Positions",
        widget=forms.Textarea,
        strip=True,
        validators=[ValidatorMaxNumberValue(max_count=4)],
    )
