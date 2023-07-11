from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import Competencies
from django.db import migrations

if TYPE_CHECKING:
    from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
    from django.db.migrations.state import StateApps

COMPETENCIES = ("Intern", "Junior", "Middle", "Senior")


def populate_competencies(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    for competence in COMPETENCIES:
        Competencies.objects.create(competence=competence)


def delete_competencies(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    for competence in COMPETENCIES:
        Competencies.objects.get(competence=competence).delete()


class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]] = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=populate_competencies, reverse_code=delete_competencies
        ),
    ]
