from django.db import models

from .base_model import BaseModel


class Countries(BaseModel):
    country = models.CharField(max_length=60, unique=True)

    class Meta:
        db_table = "countries"
