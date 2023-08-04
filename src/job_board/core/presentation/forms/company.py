from core.presentation.validators import (
    ValidateFileExtension,
    ValidatorFileSize,
    ValidatorMaxNumberValue,
)
from django import forms


class CompanyForm(forms.Form):
    company_name = forms.CharField(label='Company name', max_length=100, strip=True)
    founding_year = forms.IntegerField(label='Founding year')
    logo = forms.ImageField(
        label='Logo',
        validators=[
            ValidateFileExtension(["jpeg", "jpg", "png"]),
            ValidatorFileSize(5_000_000),
        ],
    )
    description = forms.CharField(
        label='Description', widget=forms.Textarea, strip=True
    )
    phone = forms.CharField(label='Phone', max_length=20, strip=True)
    linkedin = forms.CharField(label='Linkedin', required=False, strip=True)
    instagram = forms.CharField(label='Instagram', required=False, strip=True)
    web_site = forms.CharField(label='Web site', strip=True)
    twitter = forms.CharField(label='Twitter', required=False, strip=True)
    business_lines = forms.CharField(
        label="Business lines",
        widget=forms.Textarea,
        strip=True,
        validators=[ValidatorMaxNumberValue(max_count=4)],
    )
    staff_number = forms.IntegerField(label='Staff number', min_value=1)
    country = forms.CharField(label='Country', max_length=100, strip=True)
    city = forms.CharField(label='City', max_length=100, strip=True)
    street = forms.CharField(label='Street', max_length=100, strip=True)
    house_number = forms.IntegerField(label='House number')
    office_number = forms.IntegerField(label='Office number')
