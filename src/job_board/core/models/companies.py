from django.db import models

from .base_model import BaseModel


class Companies(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    address = models.OneToOneField(
        to="Addresses", related_name="companies", on_delete=models.CASCADE
    )
    staff_number = models.ForeignKey(
        to="StaffNumber", related_name="companies", on_delete=models.CASCADE
    )
    founding_year = models.SmallIntegerField()
    logo = models.FileField(upload_to="company/logo/", blank=True)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    web_site = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150, blank=True)
    business_lines = models.ManyToManyField(
        to="BusinessLines", through="CompaniesBusinessLines"
    )

    class Meta:
        db_table = "companies"
