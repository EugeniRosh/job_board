from django.db import models

from .base_model import BaseModel


class ResponseStatuses(BaseModel):
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "response_statuses"
