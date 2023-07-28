from core.models.base_model import BaseModel
from django.db import models


class Skills(BaseModel):
    skill = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "skills"
