from __future__ import annotations

import sys
import uuid
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import connection
from PIL import Image


def print_queries() -> None:
    queries_count = 0
    for i in connection.queries:
        print(i)
        queries_count += 1
    print()
    print(queries_count)
    print()
    return


def rename_in_uuid(file: InMemoryUploadedFile) -> InMemoryUploadedFile:
    file_extension = file.name.split(".")[-1]
    file_name = str(uuid.uuid4())
    file.name = file_name + "." + file_extension
    return file


def change_file_size(file: InMemoryUploadedFile) -> InMemoryUploadedFile:
    file_extension = file.content_type.split("/")[-1].upper()
    output = BytesIO()
    with Image.open(file) as image:
        image.thumbnail(size=(150, 100))
        image.save(fp=output, format=file_extension, quality=100)

    return InMemoryUploadedFile(
        file=output,
        field_name=file.field_name,
        name=file.name,
        content_type=file.content_type,
        size=sys.getsizeof(output),
        charset=file.charset,
    )
