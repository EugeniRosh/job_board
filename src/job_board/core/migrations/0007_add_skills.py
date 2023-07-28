from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import Skills
from django.db import migrations

if TYPE_CHECKING:
    from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
    from django.db.migrations.state import StateApps

SKILLS = ("A1", "A2", "B1", "B2", "C1", "C2")


def populate_skills(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    for skill in SKILLS:
        Skills.objects.create(skill=skill)


def delete_skills(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    for skills in SKILLS:
        Skills.objects.get(skills=skills).delete()


class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]] = [
        ('core', '0006_add_response_statuses'),
    ]

    operations = [
        migrations.RunPython(code=populate_skills, reverse_code=delete_skills),
    ]
