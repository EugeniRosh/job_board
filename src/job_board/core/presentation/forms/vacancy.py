from core.presentation.validators import ValidatorMaxNumberValue
from django import forms

from .default_values import COMPETENCE, EMPLOYMENT_FORMATS


class VacancyForm(forms.Form):
    title = forms.CharField(label='Job title', max_length=50, strip=True)
    description = forms.CharField(
        label="Description", widget=forms.Textarea, strip=True
    )
    work_format = forms.CharField(
        label="Work format",
        widget=forms.Textarea,
        strip=True,
        validators=[ValidatorMaxNumberValue(max_count=4)],
    )
    employment_formats = forms.ChoiceField(
        label="Employment formats", choices=EMPLOYMENT_FORMATS
    )
    competence = forms.ChoiceField(label='Competence', choices=COMPETENCE)
    min_experience = forms.IntegerField(label="Minimal experience", min_value=0)
    min_salary = forms.IntegerField(label='Max_salary', min_value=0)
    max_salary = forms.IntegerField(label='Max_salary', min_value=0)
    tags = forms.CharField(
        label="Tags",
        widget=forms.Textarea,
        strip=True,
        validators=[ValidatorMaxNumberValue(max_count=5)],
    )
    countries = forms.CharField(label="Countries", widget=forms.Textarea, strip=True)


class SearchVacancyForm(forms.Form):
    title = forms.CharField(
        label='Job title', max_length=50, strip=True, required=False
    )
    work_format = forms.CharField(label="Work format", strip=True, required=False)
    employment_formats = forms.ChoiceField(
        label="Employment formats",
        choices=EMPLOYMENT_FORMATS + [("", "All")],
        required=False,
    )
    competence = forms.ChoiceField(
        label='Competence', choices=COMPETENCE + [("", "All")], required=False
    )
    salary_min = forms.IntegerField(label='Mix salary', min_value=0, required=False)
    salary_max = forms.IntegerField(label='Max salary', min_value=0, required=False)
    tag = forms.CharField(label="Tags", strip=True, required=False)
    country = forms.CharField(label="Countries", strip=True, required=False)
