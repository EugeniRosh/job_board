from django.db import models

from .base_model import BaseModel


class EmployeesPositions(BaseModel):
    employee = models.ForeignKey(
        to="Employees", related_name="employees", on_delete=models.CASCADE
    )
    position = models.ForeignKey(
        to="Positions", related_name="positions", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "employees_positions"
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "position"], name="unique_employees_positions"
            )
        ]
