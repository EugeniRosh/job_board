from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import Companies, Employees

from .cities import get_city
from .common import change_file_size, rename_in_uuid
from .countries import get_country
from .positions import get_positions

if TYPE_CHECKING:
    from core.bussiness_logic.dto import EmployeeDTO


def add_employee(data: EmployeeDTO, company_id: int) -> None:
    positions = get_positions(positions=data.position)

    data.photo = rename_in_uuid(data.photo)
    data.photo = change_file_size(data.photo)

    city = get_city(request_city=data.city)
    country = get_country(request_country=data.country)
    company = Companies.objects.get(id=company_id)

    employee_db = Employees.objects.create(
        name=data.name,
        surname=data.surname,
        country=country,
        city=city,
        company=company,
        email=data.email,
        phone=data.phone,
        password=data.password,
        photo=data.photo,
    )
    employee_db.position.set(positions)

    return None


def get_employees_company(company: str) -> list[Employees]:
    employees_db = Employees.objects.prefetch_related("position").select_related(
        "country", "city", "company"
    )

    employees_db = employees_db.filter(company__name=company)

    return list(employees_db)
