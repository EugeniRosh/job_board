from django.db import models

from .base_model import BaseModel


class Reviews(BaseModel):
    user = models.ForeignKey(
        to="Users", related_name="reviews", on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        to="Companies", related_name="reviews", on_delete=models.CASCADE
    )
    review = models.TextField(max_length=800)

    class Meta:
        db_table = "reviews"
