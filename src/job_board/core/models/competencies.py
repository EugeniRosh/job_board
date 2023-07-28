from django.db import models

from .base_model import BaseModel


class Competencies(BaseModel):
    competence = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "competencies"
