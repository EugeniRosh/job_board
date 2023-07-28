from django.db import models

from .base_model import BaseModel


class Positions(BaseModel):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = "positions"
