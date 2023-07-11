from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import UserStatuses
from django.db import migrations

if TYPE_CHECKING:
    from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
    from django.db.migrations.state import StateApps

USER_STATUS = ("open to work", "open for proposals", "not open for proposals")


def populate_user_statuses(
    apps: StateApps, schema_editor: DatabaseSchemaEditor
) -> None:
    for status in USER_STATUS:
        UserStatuses.objects.create(status=status)


def delete_user_statuses(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    for status in USER_STATUS:
        UserStatuses.objects.get(status=status).delete()


class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]] = [
        ('core', '0003_add_employment_format'),
    ]

    operations = [
        migrations.RunPython(
            code=populate_user_statuses, reverse_code=delete_user_statuses
        ),
    ]
