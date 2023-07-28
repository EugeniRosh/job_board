from django.core import validators
from django.db import models

from .base_model import BaseModel


class Users(BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.SmallIntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    work_experience = models.SmallIntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    resume = models.FileField(upload_to="users/resume/", blank=True)
    photo = models.FileField(upload_to="users/photo/", blank=True)
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
    salary_min = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    salary_max = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    language = models.ManyToManyField(
        to="LanguageSkills", through="UsersLanguageSkills"
    )
    tag = models.ManyToManyField(to="Tags", through="UsersTags")

    class Meta:
        db_table = "users"
