from django.db import models

from .base_model import BaseModel


class UsersTags(BaseModel):
    user = models.ForeignKey(to="Users", related_name="Users", on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tags", related_name="Tags", on_delete=models.CASCADE)

    class Meta:
        db_table = "users_tags"
        constraints = [
            models.UniqueConstraint(fields=["user", "tag"], name="unique_users_tags")
        ]
