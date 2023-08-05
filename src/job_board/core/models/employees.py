from django.contrib.auth import get_user_model
from django.db import models

from .base_model import BaseModel


class Employees(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    country = models.ForeignKey(
        to="Countries", related_name="employees", on_delete=models.CASCADE, null=True
    )
    city = models.ForeignKey(
        to="Cities", related_name="employees", on_delete=models.CASCADE, null=True
    )
    company = models.ForeignKey(
        to="Companies", related_name="employees", on_delete=models.CASCADE, null=True
    )
    phone = models.CharField(max_length=150, blank=True)
    photo = models.CharField(max_length=150, blank=True)
    position = models.ManyToManyField(to="Positions", through="EmployeesPositions")
    auth_user = models.OneToOneField(
        to=get_user_model(), related_name="employees", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "employees"
