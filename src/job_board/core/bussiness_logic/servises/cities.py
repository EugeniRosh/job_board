from __future__ import annotations

from core.models import Cities


def get_city(request_city: str) -> Cities:
    response_city: tuple[Cities, bool] = Cities.objects.get_or_create(
        city=request_city.lower()
    )
    return response_city[0]
