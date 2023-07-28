from __future__ import annotations

from core.models import Positions


def get_positions(positions: str) -> list[Positions]:
    positions_list: list[Positions] = []
    positions_split = positions.split("\r\n")

    for position in positions_split:
        position_from_db, positions_bool = Positions.objects.get_or_create(
            title=position.lower()
        )
        positions_list.append(position_from_db)

    return positions_list
