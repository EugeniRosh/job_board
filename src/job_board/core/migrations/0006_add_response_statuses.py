from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import ResponseStatuses
from django.db import migrations

if TYPE_CHECKING:
    from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
    from django.db.migrations.state import StateApps

STATUS_JOBRESPONSE = ("created", "reviewed", "rejected", "accepted for work")


def populate_response_statuses(
    apps: StateApps, schema_editor: DatabaseSchemaEditor
) -> None:
    for status in STATUS_JOBRESPONSE:
        ResponseStatuses.objects.create(status=status)


def delete_response_statuses(
    apps: StateApps, schema_editor: DatabaseSchemaEditor
) -> None:
    for status in STATUS_JOBRESPONSE:
        ResponseStatuses.objects.get(status=status).delete()


class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]] = [
        ('core', '0005_add_genders'),
    ]

    operations = [
        migrations.RunPython(
            code=populate_response_statuses, reverse_code=delete_response_statuses
        ),
    ]
