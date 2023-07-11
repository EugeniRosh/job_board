from django.core import validators
from django.db import models


class Skills(models.Model):
    skill = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "skills"


class Languages(models.Model):
    title = models.CharField(max_length=50, unique=True)
    skill = models.ManyToManyField(to="Skills", through="LanguageSkills")

    class Meta:
        db_table = "languages"


class LanguageSkills(models.Model):
    language = models.ForeignKey(
        to="Languages", related_name="languages", on_delete=models.CASCADE
    )
    skill = models.ForeignKey(
        to="Skills", related_name="skills", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "language_skills"
        constraints = [
            models.UniqueConstraint(
                fields=["language", "skill"], name="unique_language_skills"
            )
        ]


class UserStatuses(models.Model):
    status = models.CharField(max_length=40, unique=True)

    class Meta:
        db_table = "user_statuses"


class WorkFormats(models.Model):
    work_format = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "work_formats"


class Competencies(models.Model):
    competence = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "competencies"


class EmploymentFormats(models.Model):
    employment_format = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "employment_formats"


class Salary(models.Model):
    salary_min = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    salary_max = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )

    class Meta:
        db_table = "salary"


class Tags(models.Model):
    tag = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = "tags"


class Countries(models.Model):
    country = models.CharField(max_length=60, unique=True)

    class Meta:
        db_table = "countries"


class Cities(models.Model):
    city = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "cities"


class Genders(models.Model):
    gender = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "genders"


class Profiles(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=150, blank=True)
    github = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150)  # delete
    login = models.CharField(max_length=30, unique=True)
    country = models.ForeignKey(
        to="Countries", related_name="profiles", on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        to="Cities", related_name="profiles", on_delete=models.CASCADE
    )
    gender = models.ForeignKey(
        to="Genders", related_name="profiles", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "profiles"


class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.SmallIntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    work_experience = models.SmallIntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    resume = models.TextField()
    photo = models.CharField(max_length=100, blank=True)
    experience_description = models.TextField(max_length=500)
    profile = models.OneToOneField(
        to="Profiles", related_name="users", on_delete=models.CASCADE
    )
    work_format = models.ForeignKey(
        to="WorkFormats", related_name="users", on_delete=models.CASCADE
    )
    competence = models.ForeignKey(
        to="Competencies", related_name="users", on_delete=models.CASCADE
    )
    employment_formats = models.ForeignKey(
        to="EmploymentFormats", related_name="users", on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        to="UserStatuses", related_name="users", on_delete=models.CASCADE
    )
    salary_id = models.ForeignKey(
        to="Salary", related_name="users", on_delete=models.CASCADE
    )
    language = models.ManyToManyField(to="Languages", through="UsersLanguageSkills")
    tag = models.ManyToManyField(to="Tags", through="UsersTags")

    class Meta:
        db_table = "users"


class UsersLanguageSkills(models.Model):
    user = models.ForeignKey(to="Users", related_name="users", on_delete=models.CASCADE)
    language = models.ForeignKey(
        to="Languages", related_name="LanguageSkills", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "users_language_skills"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "language"], name="unique_users_language_skills"
            )
        ]


class UsersTags(models.Model):
    user = models.ForeignKey(to="Users", related_name="Users", on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tags", related_name="Tags", on_delete=models.CASCADE)
    companies = models.ForeignKey(
        to="Companies", related_name="company", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "users_tags"
        constraints = [
            models.UniqueConstraint(fields=["user", "tag"], name="unique_users_tags")
        ]


class Addresses(models.Model):
    country = models.ForeignKey(
        to="Countries", related_name="addresses", on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        to="Cities", related_name="addresses", on_delete=models.CASCADE
    )
    street = models.CharField(max_length=100)
    house_number = models.SmallIntegerField(
        validators=[validators.MinValueValidator(limit_value=1)]
    )
    office_number = models.SmallIntegerField(
        validators=[validators.MinValueValidator(limit_value=1)]
    )

    class Meta:
        db_table = "addresses"


class StaffNumber(models.Model):
    min_staff = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=1)]
    )
    max_staff = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=1)]
    )

    class Meta:
        db_table = "staff_number"


class Companies(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.OneToOneField(
        to="Addresses", related_name="companies", on_delete=models.CASCADE
    )
    staff_number = models.ForeignKey(
        to="StaffNumber", related_name="companies", on_delete=models.CASCADE
    )
    founding_year = models.SmallIntegerField()
    logo = models.CharField(max_length=100, blank=True)  # delete
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    web_site = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150, blank=True)
    business_lines = models.ManyToManyField(
        to="BusinessLines", through="CompaniesBusinessLines"
    )

    class Meta:
        db_table = "companies"


class BusinessLines(models.Model):
    business_line = models.CharField(max_length=50)

    class Meta:
        db_table = "business_lines"


class CompaniesBusinessLines(models.Model):
    company = models.ForeignKey(
        to="Companies", related_name="companies", on_delete=models.CASCADE
    )
    business_line = models.ForeignKey(
        to="BusinessLines", related_name="BusinessLines", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "companies_business_lines"
        constraints = [
            models.UniqueConstraint(
                fields=["company", "business_line"],
                name="unique_companies_business_lines",
            )
        ]


class Positions(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = "positions"


class Employees(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    country = models.ForeignKey(
        to="Countries", related_name="employees", on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        to="Cities", related_name="employees", on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        to="Companies", related_name="employees", on_delete=models.CASCADE
    )
    email = models.EmailField()
    phone = models.CharField(max_length=150)  # delete
    password = models.CharField(max_length=150)  # delete
    photo = models.CharField(max_length=150, blank=True)  # delete
    position = models.ManyToManyField(to="Positions", through="EmployeesPositions")

    class Meta:
        db_table = "employees"


class EmployeesPositions(models.Model):
    employee = models.ForeignKey(
        to="Employees", related_name="employees", on_delete=models.CASCADE
    )
    position = models.ForeignKey(
        to="Positions", related_name="positions", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "employees_positions"
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "position"], name="unique_employees_positions"
            )
        ]


class Reviews(models.Model):
    user = models.ForeignKey(
        to="Users", related_name="reviews", on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        to="Companies", related_name="reviews", on_delete=models.CASCADE
    )
    review = models.TextField(max_length=800)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    likes = models.IntegerField(
        default=0, validators=[validators.MinValueValidator(limit_value=0)]
    )
    dislikes = models.IntegerField(
        default=0, validators=[validators.MinValueValidator(limit_value=0)]
    )

    class Meta:
        db_table = "reviews"


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employee = models.ForeignKey(
        to="Employees", related_name="vacancy", on_delete=models.CASCADE
    )
    work_format = models.ForeignKey(
        to="WorkFormats", related_name="vacancy", on_delete=models.CASCADE
    )
    competence = models.ForeignKey(
        to="Competencies", related_name="vacancy", on_delete=models.CASCADE
    )
    employment_formats = models.ForeignKey(
        to="EmploymentFormats", related_name="vacancy", on_delete=models.CASCADE
    )
    salary = models.ForeignKey(
        to="Salary", related_name="vacancy", on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(to="Tags", through="VacancyTags")
    country = models.ManyToManyField(to="Countries", through="VacancyCounties")

    class Meta:
        db_table = "vacancy"


class VacancyTags(models.Model):
    vacancy = models.ForeignKey(
        to="Vacancy", related_name="vacancies", on_delete=models.CASCADE
    )
    tag = models.ForeignKey(to="Tags", related_name="tags", on_delete=models.CASCADE)

    class Meta:
        db_table = "vacancy_tags"
        constraints = [
            models.UniqueConstraint(
                fields=["vacancy", "tag"], name="unique_vacancy_tags"
            )
        ]


class VacancyCounties(models.Model):
    vacancy = models.ForeignKey(
        to="Vacancy", related_name="vacancy", on_delete=models.CASCADE
    )
    country = models.ForeignKey(
        to="Countries", related_name="countries", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "vacancy_counties"
        constraints = [
            models.UniqueConstraint(
                fields=["vacancy", "country"], name="unique_vacancy_counties"
            )
        ]


class ResponseStatuses(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "response_statuses"


class Responses(models.Model):
    user = models.ForeignKey(
        to="Users", related_name="responses", on_delete=models.CASCADE
    )
    vacancy = models.ForeignKey(
        to="Vacancy", related_name="responses", on_delete=models.CASCADE
    )
    accompanying_text = models.TextField(max_length=500)
    resume = models.CharField(max_length=150)  # delete
    status = models.ForeignKey(
        to="ResponseStatuses", related_name="responses", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "responses"
