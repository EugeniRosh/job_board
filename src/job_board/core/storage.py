from __future__ import annotations

from dataclasses import dataclass


class VacanciesStorage:
    def __init__(self) -> None:
        self._vacancy_id = 1
        self._storage: list[VacancyDTO] = []

    def add_vacancies(self, vacancy: VacancyDTO) -> None:
        vacancy.vacancy_id = self._vacancy_id
        self._vacancy_id += 1
        self._storage.append(vacancy)

    def get_vacancies(self) -> list[VacancyDTO]:
        return self._storage


class CompaniesStorage:
    def __init__(self) -> None:
        self._company_id = 1
        self._storage: list[CompanyDTO] = []

    def add_companies(self, company: CompanyDTO) -> None:
        company.company_id = self._company_id
        self._company_id += 1
        self._storage.append(company)

    def get_companies(self) -> list[CompanyDTO]:
        return self._storage


class UsersStorage:
    def __init__(self) -> None:
        self._user_id = 1
        self._storage: list[UserDTO] = []

    def add_user(self, user: UserDTO) -> None:
        user.user_id = self._user_id
        self._user_id += 1
        self._storage.append(user)

    def get_users(self) -> list[UserDTO]:
        return self._storage


class JobResponseStorage:
    def __init__(self) -> None:
        self._response_id = 1
        self._storage: list[JobResponseDTO] = []

    def add_response(self, response: JobResponseDTO) -> None:
        response.response_id = self._response_id
        self._response_id += 1
        self._storage.append(response)

    def get_response(self) -> list[JobResponseDTO]:
        return self._storage


class CompanyReviewStorage:
    def __init__(self) -> None:
        self._response_id = 1
        self._storage: list[CompanyReviewDTO] = []

    def add_response(self, response: CompanyReviewDTO) -> None:
        response.review_id = self._response_id
        self._response_id += 1
        self._storage.append(response)

    def get_response(self) -> list[CompanyReviewDTO]:
        return self._storage


@dataclass
class VacancyDTO:
    vacancy_id: int | None
    title: str
    company: str
    competence: str
    experience: str
    min_salary: int
    max_salary: int


@dataclass
class VacancyCount:
    company: str
    count_vacancy: int


@dataclass
class CompanyDTO:
    company_id: int | None
    name: str
    founding_year: int
    logo: str
    description: str
    email: str | None
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
    count_vacancy: int = 2


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
    resume: str
    photo: str
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


@dataclass
class JobResponseDTO:
    response_id: int | None
    user: str
    vacancy_id: int | None
    accompanying_text: str
    resume: str
    user_phone: str
    status: str


@dataclass
class CompanyReviewDTO:
    review_id: int | None
    user: str
    company_id: int | None
    review: str
    likes: int
    dislikes: int


vacancies_storage = VacanciesStorage()
users_storage = UsersStorage()
companies_storage = CompaniesStorage()
job_response_storage = JobResponseStorage()
company_review_storage = CompanyReviewStorage()
