from django import forms


class VacancyForm(forms.Form):
    title = forms.CharField(label='job title', max_length=50)
    company = forms.CharField(label='company',max_length=50)
    competence = forms.CharField(label='competence',max_length=50)
    experience = forms.CharField(label='experience',max_length=50)
    min_salary = forms.CharField(label='min salary',max_length=50)
    max_salary = forms.CharField(label='max salary',max_length=50)
