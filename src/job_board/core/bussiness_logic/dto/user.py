from dataclasses import dataclass

from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class UserDTO:
    user_id: int | None
    name: str
    surname: str
    age: int
    work_format: str
    competence: str
    design_format: str
    status: str
    work_experience: int
    resume: InMemoryUploadedFile
    photo: InMemoryUploadedFile
    experience_description: str
    min_salary: int
    max_salary: int
    email: str
    phone: str
    country: str
    city: str
    linkedin: str | None
    github: str | None
    password: str
    login: str
    gender: str
    tags: str
    language: str
    language_skill: str
