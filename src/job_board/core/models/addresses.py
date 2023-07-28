from django.core import validators
from django.db import models

from .base_model import BaseModel


class Addresses(BaseModel):
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
