from django.db import models

from .base_model import BaseModel


class Employees(BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    country = models.ForeignKey(
        to="Countries", related_name="employees", on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        to="Cities", related_name="employees", on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        to="Companies", related_name="employees", on_delete=models.CASCADE
    )
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    photo = models.CharField(max_length=150, blank=True)
    position = models.ManyToManyField(to="Positions", through="EmployeesPositions")

    class Meta:
        db_table = "employees"
