from django.core import validators
from django.db import models

from .base_model import BaseModel


class Vacancy(BaseModel):
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
    salary_min = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    salary_max = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=0)]
    )
    tag = models.ManyToManyField(to="Tags", through="VacancyTags")
    country = models.ManyToManyField(to="Countries", through="VacancyCountries")

    class Meta:
        db_table = "vacancy"
