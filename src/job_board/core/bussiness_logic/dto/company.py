from dataclasses import dataclass

from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class CompanyDTO:
    company_name: str | None
    founding_year: int | None
    logo: InMemoryUploadedFile | None
    description: str | None
    business_lines: str
    phone: str
    linkedin: str | None
    instagram: str | None
    web_site: str
    twitter: str | None
    staff_number: int
    country: str
    city: str
    street: str
    house_number: int
    office_number: int
