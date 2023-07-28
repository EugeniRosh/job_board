from __future__ import annotations

from typing import TYPE_CHECKING

from core.bussiness_logic.exeptions import CreateUniqueError, ValueNotExists
from core.models import Addresses, Companies
from django.db.models import Count
from django.db.utils import IntegrityError

from .business_lines import get_business_lines
from .cities import get_city
from .common import change_file_size, rename_in_uuid
from .countries import get_country
from .staff_number import get_staff

if TYPE_CHECKING:
    from core.bussiness_logic.dto import CompanyDTO
    from core.models import BusinessLines


def add_company(company: CompanyDTO) -> None:
    country_db = get_country(request_country=company.country)
    city_db = get_city(request_city=company.city)
    lines_lst = get_business_lines(business_lines=company.business_lines)
    staff_db = get_staff(min_staff=company.min_staff, max_staff=company.max_staff)

    company.logo = rename_in_uuid(file=company.logo)
    company.logo = change_file_size(file=company.logo)

    try:
        company_db = Companies.objects.create(
            name=company.name.lower(),
            founding_year=company.founding_year,
            logo=company.logo,
            description=company.description.lower(),
            email=company.email,
            phone=company.phone,
            staff_number=staff_db,
            linkedin=company.linkedin,
            instagram=company.instagram,
            web_site=company.web_site.lower(),
            twitter=company.twitter,
            address=Addresses.objects.create(
                country=country_db,
                city=city_db,
                street=company.street.lower(),
                house_number=company.house_number,
                office_number=company.office_number,
            ),
        )

        company_db.business_lines.set(lines_lst)
    except IntegrityError:
        raise CreateUniqueError

    return None


def get_all_company() -> list[Companies]:
    companies_db = (
        Companies.objects.annotate(count_vacancies=Count("employees__vacancy__id"))
        .values("name", "count_vacancies", "id")
        .order_by("-count_vacancies")
    )

    return list(companies_db)


def get_company_by_id(company_id: int) -> tuple[Companies, list[BusinessLines]]:
    try:
        company = (
            Companies.objects.prefetch_related("business_lines")
            .select_related("address", "staff_number")
            .get(id=company_id)
        )
        business_lines = company.business_lines.all()
    except Companies.DoesNotExist:
        raise ValueNotExists

    return company, list(business_lines)
