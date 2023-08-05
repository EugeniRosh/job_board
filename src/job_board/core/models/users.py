from django.contrib.auth import get_user_model
from django.db import models

from .base_model import BaseModel


class Users(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    age = models.PositiveSmallIntegerField(null=True)
    work_experience = models.PositiveIntegerField(null=True)
    resume = models.FileField(upload_to="users/resume/", blank=True)
    photo = models.FileField(upload_to="users/photo/", blank=True)
    experience_description = models.TextField(max_length=500, blank=True)
    work_format = models.ForeignKey(
        to="WorkFormats", related_name="users", on_delete=models.CASCADE, null=True
    )
    competence = models.ForeignKey(
        to="Competencies", related_name="users", on_delete=models.CASCADE, null=True
    )
    employment_formats = models.ForeignKey(
        to="EmploymentFormats",
        related_name="users",
        on_delete=models.CASCADE,
        null=True,
    )
    status = models.ForeignKey(
        to="UserStatuses",
        related_name="users",
        on_delete=models.CASCADE,
        null=True,
    )
    salary_min = models.PositiveIntegerField(null=True)
    salary_max = models.PositiveIntegerField(null=True)
    language = models.ManyToManyField(
        to="LanguageSkills", through="UsersLanguageSkills"
    )
    tag = models.ManyToManyField(to="Tags", through="UsersTags")
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.CharField(max_length=150, blank=True)
    github = models.CharField(max_length=150, blank=True)
    country = models.ForeignKey(
        to="Countries", related_name="profiles", on_delete=models.CASCADE, null=True
    )
    city = models.ForeignKey(
        to="Cities", related_name="profiles", on_delete=models.CASCADE, null=True
    )
    gender = models.ForeignKey(
        to="Genders", related_name="profiles", on_delete=models.CASCADE, null=True
    )
    auth_user = models.OneToOneField(
        to=get_user_model(), related_name="users", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "users"
