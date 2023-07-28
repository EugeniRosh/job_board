from __future__ import annotations

from core.models import BusinessLines


def get_business_lines(business_lines: str) -> list[BusinessLines]:
    lines: list[str] = business_lines.split("\r\n")
    lines_lst: list[BusinessLines] = []
    for line in lines:
        business_lines_db: tuple[
            BusinessLines, bool
        ] = BusinessLines.objects.get_or_create(business_line=line.lower())
        lines_lst.append(business_lines_db[0])

    return lines_lst
