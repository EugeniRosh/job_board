from __future__ import annotations

from typing import TYPE_CHECKING

from core.bussiness_logic.exeptions import ValueNotExists
from core.models import Competencies, Employees, EmploymentFormats, Vacancy

from .countries import get_countries_vacancy
from .tags import get_tags
from .work_format import get_work_format

if TYPE_CHECKING:
    from core.bussiness_logic.dto import SearchVacancyDTO, VacancyDTO
    from core.models import Countries, Tags


def add_vacancy(data: VacancyDTO, employee_id: int) -> None:
    employment_formats = EmploymentFormats.objects.get(
        employment_format=data.employment_formats
    )
    competence = Competencies.objects.get(competence=data.competence)
    work_format = get_work_format(request_work_format=data.work_format)
    employee = Employees.objects.get(id=employee_id)

    vacancy_db = Vacancy.objects.create(
        title=data.title.lower(),
        description=data.description.lower(),
        employee=employee,
        work_format=work_format,
        employment_formats=employment_formats,
        competence=competence,
        salary_min=data.min_salary,
        salary_max=data.max_salary,
    )

    tags = get_tags(respons_tags=data.tags)
    vacancy_db.tag.set(tags)

    countries = get_countries_vacancy(countries=data.countries)
    vacancy_db.country.set(countries)

    return None


def get_all_vacancy(search_filters: SearchVacancyDTO) -> list[Vacancy]:
    vacancies = (
        Vacancy.objects.select_related("employee", "competence")
        .values(
            "id",
            "title",
            "salary_min",
            "salary_max",
            "competence__competence",
            "employee__company__name",
        )
        .order_by("-update_at")
    )
    if search_filters.title:
        vacancies = vacancies.filter(title__icontains=search_filters.title)

    if search_filters.competence:
        vacancies = vacancies.filter(competence__competence=search_filters.competence)

    if search_filters.country:
        vacancies = vacancies.filter(country__country=search_filters.country)

    if search_filters.employment_formats:
        vacancies = vacancies.filter(
            employment_formats__employment_format=search_filters.employment_formats
        )

    if search_filters.work_format:
        vacancies = vacancies.filter(
            work_format__work_format__icontains=search_filters.work_format
        )

    if search_filters.salary_min:
        vacancies = vacancies.filter(salary_min__gte=search_filters.salary_min)

    if search_filters.salary_max:
        vacancies = vacancies.filter(salary_max__lte=search_filters.salary_max)

    return list(vacancies)


def get_vacancy_by_id(vacancy_id: int) -> tuple[Vacancy, list[Tags], list[Countries]]:
    try:
        vacancy = (
            Vacancy.objects.prefetch_related("tag", "country")
            .select_related(
                "employee", "work_format", "competence", "employment_formats"
            )
            .get(id=vacancy_id)
        )
        tags = vacancy.tag.all()
        countries = vacancy.country.all()

    except Vacancy.DoesNotExist:
        raise ValueNotExists

    return vacancy, list(tags), list(countries)
