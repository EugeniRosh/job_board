from core.presentation.validators import (
    ValidateFileExtension,
    ValidatorFileSize,
    ValidatorMaxNumberValue,
)
from django import forms


class EmployeesForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, strip=True, required=False)
    surname = forms.CharField(
        label="Surname", max_length=50, strip=True, required=False
    )
    photo = forms.ImageField(
        label="Photo",
        required=False,
        validators=[
            ValidateFileExtension(["jpeg", "jpg", "png"]),
            ValidatorFileSize(5_000_000),
        ],
    )
    country = forms.CharField(
        label="Country", max_length=100, strip=True, required=False
    )
    city = forms.CharField(label="City", max_length=100, strip=True, required=False)
    phone = forms.CharField(label="Phone", max_length=20, strip=True)
    position = forms.CharField(
        label="Positions",
        widget=forms.Textarea,
        required=False,
        strip=True,
        validators=[ValidatorMaxNumberValue(max_count=4)],
    )
