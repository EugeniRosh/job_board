from django import forms

from .default_values import STATUS_JOBRESPONSE


class VacancyResponseForm(forms.Form):
    user = forms.CharField(label="User")
    accompanying_text = forms.CharField(
        label="Accompanying text", max_length=500, widget=forms.Textarea, strip=True
    )
    resume = forms.CharField(label="Resume")
    user_phone = forms.CharField(label="Phone")
    status = forms.ChoiceField(label="Feedback status", choices=STATUS_JOBRESPONSE)
