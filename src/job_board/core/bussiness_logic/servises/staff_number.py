from __future__ import annotations

from core.models import StaffNumber


def get_staff(min_staff: int, max_staff: int) -> StaffNumber:
    response_staff: tuple[StaffNumber, bool] = StaffNumber.objects.get_or_create(
        min_staff=min_staff, max_staff=max_staff
    )
    return response_staff[0]
