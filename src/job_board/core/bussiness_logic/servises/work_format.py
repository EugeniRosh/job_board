from __future__ import annotations

from core.models import WorkFormats


def get_work_format(request_work_format: str) -> WorkFormats:
    response_work_format: tuple[WorkFormats, bool] = WorkFormats.objects.get_or_create(
        work_format=request_work_format.lower()
    )
    return response_work_format[0]
