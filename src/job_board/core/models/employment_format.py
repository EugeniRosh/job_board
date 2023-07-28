from django.db import models

from .base_model import BaseModel


class EmploymentFormats(BaseModel):
    employment_format = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "employment_formats"
