from django import forms

STATUS_VACANCY = (
    ("open to work", "open to work"),
    ("open for proposals", "open for proposals"),
    ("not open for proposals", "not open for proposals"),
)

STATUS_JOBRESPONSE = (
    ("created", "created"),
    ("reviewed", "reviewed"),
    ("rejected", "rejected"),
    ("accepted for work", "accepted for work"),
)


class VacancyForm(forms.Form):
    title = forms.CharField(label='Job title', max_length=50)
    company = forms.CharField(label='Company')
    competence = forms.CharField(label='Competence', max_length=50)
    experience = forms.CharField(label='Experience', max_length=50)
    min_salary = forms.IntegerField(label='Max_salary', min_value=1)
    max_salary = forms.IntegerField(label='Max_salary', min_value=1)


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
    min_staff = forms.IntegerField(label='Min_staff', min_value=1)
    max_staff = forms.IntegerField(label='Max_staff', min_value=1)
    country = forms.CharField(label='Country', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    street = forms.CharField(label='Street', max_length=100)
    house_number = forms.IntegerField(label='House number')
    office_number = forms.IntegerField(label='Office number')


class UserForm(forms.Form):
    name = forms.CharField(label='Name')
    surname = forms.CharField(label='Surname', max_length=50)
    age = forms.IntegerField(label='Age', min_value=0, required=False)
    work_format = forms.CharField(label='Work format')
    competence = forms.CharField(label='Competence')
    design_format = forms.CharField(label='Design format')
    status = forms.ChoiceField(label='Status', choices=STATUS_VACANCY)
    work_experience = forms.IntegerField(
        label='Work experience', min_value=0, required=False
    )
    resume = forms.CharField(label='Resume')
    photo = forms.CharField(label='Photo')
    experience_description = forms.CharField(
        label='Experience description', max_length=200
    )
    min_salary = forms.IntegerField(label='Min salary', min_value=0, required=False)
    max_salary = forms.IntegerField(label='Max salary', min_value=0, required=False)
    email = forms.EmailField(label='Email', max_length=50)
    phone = forms.CharField(label='Phone', max_length=20)
    country = forms.CharField(label='Country')
    city = forms.CharField(label='City')
    linkedin = forms.CharField(label='Linkedin', required=False)
    github = forms.CharField(label='Github', required=False)
    password = forms.CharField(label='Password')
    login = forms.CharField(label='Login', max_length=30)
    gender = forms.CharField(label='Gender', max_length=20)


class JobResponseForm(forms.Form):
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
