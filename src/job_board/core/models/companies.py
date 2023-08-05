from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .base_model import BaseModel


class Companies(BaseModel, AbstractBaseUser):
    company_name = models.CharField(max_length=100, unique=True, blank=True)
    address = models.OneToOneField(
        to="Addresses", related_name="companies", on_delete=models.CASCADE, null=True
    )
    staff_number = models.PositiveIntegerField(null=True)
    founding_year = models.SmallIntegerField(null=True)
    logo = models.FileField(upload_to="company/logo/", blank=True)
    description = models.TextField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    web_site = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    business_lines = models.ManyToManyField(
        to="BusinessLines", through="CompaniesBusinessLines"
    )
    auth_user = models.OneToOneField(
        to=get_user_model(), related_name="companies", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "companies"
