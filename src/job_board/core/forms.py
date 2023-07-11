from core.models import (
    Competencies,
    EmploymentFormats,
    Genders,
    ResponseStatuses,
    UserStatuses,
)
from django import forms

STATUS_JOBRESPONSE = [
    (status.status, status.status) for status in ResponseStatuses.objects.all()
]
COMPETENCE = [
    (competence.competence, competence.competence)
    for competence in Competencies.objects.all()
]
USER_STATUS = [(status.status, status.status) for status in UserStatuses.objects.all()]
GENDERS = [(gender.gender, gender.gender) for gender in Genders.objects.all()]
EMPLOYMENT_FORMATS = [
    (value.employment_format, value.employment_format)
    for value in EmploymentFormats.objects.all()
]


class VacancyForm(forms.Form):
    title = forms.CharField(label='Job title', max_length=50)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    company = forms.CharField(label='Company')
    work_format = forms.CharField(label="Work format", widget=forms.Textarea)
    employment_formats = forms.ChoiceField(
        label="Employment formats", choices=EMPLOYMENT_FORMATS
    )
    competence = forms.ChoiceField(label='Competence', choices=COMPETENCE)
    min_salary = forms.IntegerField(label='Max_salary', min_value=1)
    max_salary = forms.IntegerField(label='Max_salary', min_value=1)
    tags = forms.CharField(label="Tags", widget=forms.Textarea)
    countries = forms.CharField(label="Countries", widget=forms.Textarea)


class CompanyForm(forms.Form):
    name = forms.CharField(label='Company name', max_length=100)
    founding_year = forms.IntegerField(label='Founding year')
    logo = forms.CharField(label='Logo')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Phone', max_length=20)
    linkedin = forms.CharField(label='Linkedin', required=False)
    instagram = forms.CharField(label='Instagram', required=False)
    web_site = forms.CharField(label='Web site')
    twitter = forms.CharField(label='Twitter', required=False)
    business_lines = forms.CharField(label="Business lines", widget=forms.Textarea)
    min_staff = forms.IntegerField(label='Min_staff', min_value=1)
    max_staff = forms.IntegerField(label='Max_staff', min_value=1)
    country = forms.CharField(label='Country', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    street = forms.CharField(label='Street', max_length=100)
    house_number = forms.IntegerField(label='House number')
    office_number = forms.IntegerField(label='Office number')


class UserForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    surname = forms.CharField(label="Surname", max_length=50)
    age = forms.IntegerField(label="Age", min_value=0)
    work_experience = forms.IntegerField(label="Work experience", min_value=0)
    resume = forms.CharField(label="Resume")
    photo = forms.CharField(label="Photo", required=False)
    experience_description = forms.CharField(
        label="Experience description", max_length=500, widget=forms.Textarea
    )
    work_format = forms.CharField(label="Work format", widget=forms.Textarea)
    competence = forms.ChoiceField(label="Competence", choices=COMPETENCE)
    employment_formats = forms.ChoiceField(
        label="Employment formats", choices=EMPLOYMENT_FORMATS
    )
    status = forms.ChoiceField(label="Status", choices=USER_STATUS)
    min_salary = forms.IntegerField(label='Min salary', min_value=0, required=False)
    max_salary = forms.IntegerField(label='Max salary', min_value=0, required=False)
    language = forms.CharField(label="Languages", max_length=500, widget=forms.Textarea)
    tags = forms.CharField(label="Tags", max_length=500, widget=forms.Textarea)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=20)
    linkedin = forms.CharField(label="", max_length=150, required=False)
    github = forms.CharField(label="", max_length=150, required=False)
    password = forms.CharField(label="", max_length=150)
    login = forms.CharField(label="", max_length=30)
    country = forms.CharField(label="Country", max_length=20)
    city = forms.CharField(label="City", max_length=20)
    gender = forms.ChoiceField(label="Gender", choices=GENDERS)


class VacancyResponseForm(forms.Form):
    user = forms.CharField(label="User")
    accompanying_text = forms.CharField(
        label="Accompanying text", max_length=500, widget=forms.Textarea
    )
    resume = forms.CharField(label="Resume")
    user_phone = forms.CharField(label="Phone")
    status = forms.ChoiceField(label="Feedback status", choices=STATUS_JOBRESPONSE)


class CompanyReviewForm(forms.Form):
    user = forms.CharField(label="User")
    review = forms.CharField(
        label="Accompanying text", max_length=800, widget=forms.Textarea
    )
    likes = forms.BooleanField(label="Like")
    dislikes = forms.BooleanField(label="Dislikes")
