from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import EmploymentFormats
from django.db import migrations

EMPLOYMENT_FORMATS = ("employment contract", "B2B", "mandate contrac")

if TYPE_CHECKING:
    from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
    from django.db.migrations.state import StateApps


def populate_employment_formats(
    apps: StateApps, schema_editor: DatabaseSchemaEditor
) -> None:
    for value in EMPLOYMENT_FORMATS:
        EmploymentFormats.objects.create(employment_format=value)


def delete_employment_formats(
    apps: StateApps, schema_editor: DatabaseSchemaEditor
) -> None:
    for value in EMPLOYMENT_FORMATS:
        EmploymentFormats.objects.get(employment_format=value).delete()


class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]] = [
        ('core', '0002_add_competence'),
    ]

    operations = [
        migrations.RunPython(
            code=populate_employment_formats, reverse_code=delete_employment_formats
        ),
    ]
