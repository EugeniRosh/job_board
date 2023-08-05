from typing import Any

from dacite import from_dict


def converter_data_from_dto(dto: Any, data: dict[str, Any]) -> Any:
    response = from_dict(dto, data)
    return response
