from django.db import models

from .base_model import BaseModel


class VacancyTags(BaseModel):
    vacancy = models.ForeignKey(
        to="Vacancy", related_name="vacancies", on_delete=models.CASCADE
    )
    tag = models.ForeignKey(to="Tags", related_name="tags", on_delete=models.CASCADE)

    class Meta:
        db_table = "vacancy_tags"
        constraints = [
            models.UniqueConstraint(
                fields=["vacancy", "tag"], name="unique_vacancy_tags"
            )
        ]
