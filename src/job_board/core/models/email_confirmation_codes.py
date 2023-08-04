from django.contrib.auth import get_user_model
from django.db import models

from .base_model import BaseModel


class EmailConfirmationCodes(BaseModel):
    code = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(
        to=get_user_model(),
        related_name="emailcondirmationcodes",
        on_delete=models.CASCADE,
    )
    expiration = models.PositiveIntegerField()

    class Meta:
        db_table = "emailcondirmationcodes"
