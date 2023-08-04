from dataclasses import dataclass

from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class EmployeeDTO:
    name: str | None
    surname: str | None
    login: str | None
    photo: InMemoryUploadedFile | None
    country: str | None
    city: str | None
    phone: str | None
    position: str | None
