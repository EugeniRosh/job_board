from django.db import models

from .base_model import BaseModel


class VacancyCountries(BaseModel):
    vacancy = models.ForeignKey(
        to="Vacancy", related_name="vacancy", on_delete=models.CASCADE
    )
    country = models.ForeignKey(
        to="Countries", related_name="countries", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "vacancy_counties"
        constraints = [
            models.UniqueConstraint(
                fields=["vacancy", "country"], name="unique_vacancy_counties"
            )
        ]
