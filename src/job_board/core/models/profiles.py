from django.db import models

from .base_model import BaseModel


class Profiles(BaseModel):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=150, blank=True)
    github = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150)
    login = models.CharField(max_length=30, unique=True)
    country = models.ForeignKey(
        to="Countries", related_name="profiles", on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        to="Cities", related_name="profiles", on_delete=models.CASCADE
    )
    gender = models.ForeignKey(
        to="Genders", related_name="profiles", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "profiles"
