from dataclasses import dataclass


@dataclass
class VacancyDTO:
    title: str
    description: str
    work_format: str
    employment_formats: str
    competence: str
    min_experience: int
    min_salary: int
    max_salary: int
    tags: str
    countries: str


@dataclass
class SearchVacancyDTO:
    title: str | None
    work_format: str | None
    employment_formats: str | None
    competence: str | None
    salary_min: int | None
    salary_max: int | None
    country: str | None
