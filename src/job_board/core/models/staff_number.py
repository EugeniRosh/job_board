from django.core import validators
from django.db import models

from .base_model import BaseModel


class StaffNumber(BaseModel):
    min_staff = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=1)]
    )
    max_staff = models.IntegerField(
        validators=[validators.MinValueValidator(limit_value=1)]
    )

    class Meta:
        db_table = "staff_number"
