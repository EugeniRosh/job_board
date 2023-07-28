from django.db import models

from .base_model import BaseModel


class UsersLanguageSkills(BaseModel):
    user = models.ForeignKey(to="Users", related_name="users", on_delete=models.CASCADE)
    language = models.ForeignKey(
        to="LanguageSkills", related_name="LanguageSkills", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "users_language_skills"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "language"], name="unique_users_language_skills"
            )
        ]
