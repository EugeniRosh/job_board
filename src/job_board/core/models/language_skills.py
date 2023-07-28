from django.db import models

from .base_model import BaseModel


class LanguageSkills(BaseModel):
    language = models.ForeignKey(
        to="Languages", related_name="languages", on_delete=models.CASCADE
    )
    skill = models.ForeignKey(
        to="Skills", related_name="skills", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "language_skills"
        constraints = [
            models.UniqueConstraint(
                fields=["language", "skill"], name="unique_language_skills"
            )
        ]
