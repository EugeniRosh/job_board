from django.db import models

from .base_model import BaseModel


class ReviewsScore(BaseModel):
    user = models.ForeignKey(
        to="users", related_name="reviewsscore", on_delete=models.CASCADE
    )
    review = models.ForeignKey(
        to="reviews", related_name="reviewsscore", on_delete=models.CASCADE
    )
    likes = models.BooleanField(default=False)
    dislikes = models.BooleanField(default=False)

    class Meta:
        db_table = "reviews_score"
