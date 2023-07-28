from __future__ import annotations

from core.models import Tags


def get_tags(respons_tags: str) -> list[Tags]:
    tags_list: list[Tags] = []
    tags = respons_tags.split("\r\n")

    for tag in tags:
        tag_from_db, tag_bool = Tags.objects.get_or_create(tag=tag.lower())

        tags_list.append(tag_from_db)

    return tags_list
