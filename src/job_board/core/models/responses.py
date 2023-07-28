from django.db import models

from .base_model import BaseModel


class Responses(BaseModel):
    user = models.ForeignKey(
        to="Users", related_name="responses", on_delete=models.CASCADE
    )
    vacancy = models.ForeignKey(
        to="Vacancy", related_name="responses", on_delete=models.CASCADE
    )
    accompanying_text = models.TextField(max_length=500)
    resume = models.CharField(max_length=150)  # delete
    status = models.ForeignKey(
        to="ResponseStatuses", related_name="responses", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "responses"
