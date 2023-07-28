from django.db import models

from .base_model import BaseModel


class CompaniesBusinessLines(BaseModel):
    company = models.ForeignKey(
        to="Companies", related_name="companies", on_delete=models.CASCADE
    )
    business_line = models.ForeignKey(
        to="BusinessLines", related_name="BusinessLines", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "companies_business_lines"
        constraints = [
            models.UniqueConstraint(
                fields=["company", "business_line"],
                name="unique_companies_business_lines",
            )
        ]
