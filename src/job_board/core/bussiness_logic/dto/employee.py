from dataclasses import dataclass

from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class EmployeeDTO:
    name: str
    surname: str
    photo: InMemoryUploadedFile
    country: str
    city: str
    email: str
    phone: str
    password: str
    position: str
