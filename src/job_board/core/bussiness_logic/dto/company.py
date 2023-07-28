from dataclasses import dataclass

from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class CompanyDTO:
    company_id: int | None
    name: str
    founding_year: int
    logo: InMemoryUploadedFile
    description: str
    email: str | None
    business_lines: str
    phone: str
    linkedin: str | None
    instagram: str | None
    web_site: str
    twitter: str | None
    min_staff: int
    max_staff: int
    country: str
    city: str
    street: str
    house_number: int
    office_number: int
