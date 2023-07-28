from django.db import models

from .base_model import BaseModel


class Languages(BaseModel):
    title = models.CharField(max_length=50, unique=True)
    skill = models.ManyToManyField(to="Skills", through="LanguageSkills")

    class Meta:
        db_table = "languages"
