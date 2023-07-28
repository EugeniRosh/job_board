from django.db import models

from .base_model import BaseModel


class BusinessLines(BaseModel):
    business_line = models.CharField(max_length=50)

    class Meta:
        db_table = "business_lines"
