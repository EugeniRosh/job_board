from django.db import models

from .base_model import BaseModel


class Genders(BaseModel):
    gender = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "genders"
