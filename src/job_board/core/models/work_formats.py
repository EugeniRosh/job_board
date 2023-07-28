from django.db import models

from .base_model import BaseModel


class WorkFormats(BaseModel):
    work_format = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "work_formats"
