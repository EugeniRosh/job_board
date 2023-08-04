from dataclasses import dataclass

from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class UserDTO:
    name: str | None
    surname: str | None
    login: str | None
    age: int | None
    work_format: str | None
    competence: str | None
    design_format: str | None
    status: str | None
    work_experience: int | None
    resume: InMemoryUploadedFile | None
    photo: InMemoryUploadedFile | None
    experience_description: str | None
    min_salary: int | None
    max_salary: int | None
    phone: str | None
    country: str | None
    city: str | None
    linkedin: str | None | None
    github: str | None | None
    gender: str | None
    tags: str | None
    language: str | None
    language_skill: str | None
