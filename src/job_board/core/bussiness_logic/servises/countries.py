from __future__ import annotations

from core.models import Countries


def get_country(request_country: str) -> Countries:
    response_country: tuple[Countries, bool] = Countries.objects.get_or_create(
        country=request_country.lower()
    )
    return response_country[0]


def get_countries_vacancy(countries: str) -> list[Countries]:
    countries_list: list[Countries] = []
    countries_split = countries.split("\r\n")

    for country in countries_split:
        country_db = get_country(request_country=country)
        countries_list.append(country_db)

    return countries_list
