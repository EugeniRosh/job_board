from core.presentation.validators import (
    ValidateFileExtension,
    ValidatorFileSize,
    ValidatorMaxNumberValue,
)
from django import forms

from .default_values import COMPETENCE, EMPLOYMENT_FORMATS, GENDERS, SKILLS, USER_STATUS


class UserForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, strip=True, required=False)
    surname = forms.CharField(
        label="Surname", max_length=50, strip=True, required=False
    )
    age = forms.IntegerField(label="Age", min_value=0, required=False)
    work_experience = forms.IntegerField(
        label="Work experience", min_value=0, required=False
    )
    resume = forms.FileField(
        label="Resume",
        required=False,
        validators=[ValidatorFileSize(5_000_000), ValidateFileExtension(["pdf"])],
    )
    photo = forms.ImageField(
        label="Photo",
        required=False,
        validators=[
            ValidateFileExtension(["jpeg", "jpg", "png"]),
            ValidatorFileSize(5_000_000),
        ],
    )
    experience_description = forms.CharField(
        label="Experience description",
        required=False,
        max_length=500,
        widget=forms.Textarea,
        strip=True,
    )
    work_format = forms.CharField(
        label="Work format",
        widget=forms.Textarea,
        strip=True,
        validators=[ValidatorMaxNumberValue(max_count=4)],
        required=False,
    )
    competence = forms.ChoiceField(
        label="Competence", choices=COMPETENCE, required=False
    )
    design_format = forms.ChoiceField(
        label="Employment formats", choices=EMPLOYMENT_FORMATS, required=False
    )
    status = forms.ChoiceField(label="Status", choices=USER_STATUS, required=False)
    min_salary = forms.IntegerField(label='Min salary', min_value=0, required=False)
    max_salary = forms.IntegerField(label='Max salary', min_value=0, required=False)
    language = forms.CharField(
        label="Languages",
        max_length=500,
        widget=forms.Textarea,
        required=False,
        strip=True,
    )
    language_skill = forms.ChoiceField(
        label="Language skill", choices=SKILLS, required=False
    )
    tags = forms.CharField(
        label="Tags",
        max_length=500,
        widget=forms.Textarea,
        required=False,
        strip=True,
        validators=[ValidatorMaxNumberValue(max_count=5)],
    )
    phone = forms.CharField(label="Phone", max_length=20, strip=True, required=False)
    linkedin = forms.CharField(
        label="linkedin", max_length=150, required=False, strip=True
    )
    github = forms.CharField(label="github", max_length=150, required=False, strip=True)
    country = forms.CharField(
        label="Country", max_length=20, strip=True, required=False
    )
    city = forms.CharField(label="City", max_length=20, strip=True, required=False)
    gender = forms.ChoiceField(label="Gender", choices=GENDERS, required=False)
