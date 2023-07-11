from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import Genders
from django.db import migrations

if TYPE_CHECKING:
    from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
    from django.db.migrations.state import StateApps

GENDERS = ("man", "woman")


def populate_genders(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    for gender in GENDERS:
        Genders.objects.create(gender=gender)


def delete_genders(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    for gender in GENDERS:
        Genders.objects.get(gender=gender).delete()


class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]] = [
        ('core', '0004_add_user_status'),
    ]

    operations = [
        migrations.RunPython(code=populate_genders, reverse_code=delete_genders),
    ]
