from __future__ import annotations

from typing import TYPE_CHECKING

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import VacancyForm
from .storage import Vacancy, VacancyCount, vacancies

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.http.response import HttpResponse


@require_http_methods(["GET"])
def index_controller(request: WSGIRequest) -> HttpResponse:
    context = {
        "title": "JOB BOARD",
        "index": "index",
        "vacancies": vacancies.get_vacancies,
    }
    return render(request, "core/index.html", context=context)


@require_http_methods(["GET", "POST"])
def add_core_controller(request: WSGIRequest) -> HttpResponse:
    if request.POST:
        vacancies.add_vacancies(
            vacancy=Vacancy(
                title=request.POST["title"],
                company=request.POST["company"],
                competence=request.POST["competence"],
                experience=request.POST["experience"],
                min_salary=request.POST["min_salary"],
                max_salary=request.POST["max_salary"],
            )
        )
    form = VacancyForm()
    context = {"title": "Post a job", "form": form}
    return render(request, "core/add_core.html", context=context)


@require_http_methods(["GET", "POST"])
def companies_core_controller(request: WSGIRequest) -> HttpResponse:
    companies = []
    for vacancy in vacancies.get_vacancies():
        companies.append(vacancy.company)

    count_vacancy = []
    for company in set(companies):
        count_vacancy.append(
            VacancyCount(company=company, count_vacancy=companies.count(company))
        )
    context = {"title": "Companies", "count": count_vacancy}
    return render(request, "core/companies_core.html", context=context)
