from django.db import models

from .base_model import BaseModel


class UserStatuses(BaseModel):
    status = models.CharField(max_length=40, unique=True)

    class Meta:
        db_table = "user_statuses"
