from __future__ import annotations

from typing import TYPE_CHECKING

from core.forms import (
    CompanyForm,
    CompanyReviewForm,
    UserForm,
    VacancyForm,
    VacancyResponseForm,
)
from core.storage import (
    CompanyDTO,
    CompanyReviewDTO,
    JobResponseDTO,
    UserDTO,
    VacancyDTO,
    companies_storage,
    company_review_storage,
    job_response_storage,
    users_storage,
    vacancies_storage,
)
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.http.response import HttpResponse

from dacite import from_dict


@require_http_methods(["GET"])
def index_controller(request: WSGIRequest) -> HttpResponse:
    context = {
        "title": "JOB BOARD",
        "vacancies": vacancies_storage.get_vacancies,
    }
    return render(request, "core/index.html", context=context)


@require_http_methods(["GET", "POST"])
def add_vacancy_core_controller(request: WSGIRequest) -> HttpResponse:
    if request.POST:
        form_vacancy = VacancyForm(data=request.POST)
        if form_vacancy.is_valid():
            vacancy = from_dict(VacancyDTO, form_vacancy.cleaned_data)
            vacancies_storage.add_vacancies(vacancy)
    form = VacancyForm()
    context = {"title": "Post a job", "form": form}
    return render(request, "core/add_vacancy_core.html", context=context)


@require_http_methods(["GET", "POST"])
def companies_core_controller(request: WSGIRequest) -> HttpResponse:
    company_list = companies_storage.get_companies()
    context = {"title": "Companies", "company_list": company_list}
    return render(request, "core/companies_core.html", context=context)


@require_http_methods(["GET", "POST"])
def add_company_core_controller(request: WSGIRequest) -> HttpResponse:
    if request.POST:
        form_user = CompanyForm(data=request.POST)
        if form_user.is_valid():
            company = from_dict(CompanyDTO, form_user.cleaned_data)
            companies_storage.add_companies(company)
    form = CompanyForm()
    context = {"title": "Add Company", "form": form}
    return render(request, "core/add_company_core.html", context=context)


@require_http_methods(["GET"])
def users_profile_core_controller(request: WSGIRequest) -> HttpResponse:
    print(users_storage.get_users())
    context = {"title": "Users profile", "users": users_storage.get_users}
    return render(request, "core/user_profile_core.html", context=context)


@require_http_methods(["GET", "POST"])
def add_users_profile_core_controller(request: WSGIRequest) -> HttpResponse:
    if request.POST:
        form_user = UserForm(data=request.POST)
        if form_user.is_valid():
            user = from_dict(UserDTO, form_user.cleaned_data)
            users_storage.add_user(user)

    form = UserForm()
    context = {"title": "Add users profile", "form": form}
    return render(request, "core/add_user_profile_core.html", context=context)


@require_http_methods(["GET"])
def get_vacancy_core_controller(request: WSGIRequest, vacancy_id: int) -> HttpResponse:
    for value in vacancies_storage.get_vacancies():
        if value.vacancy_id == vacancy_id:
            vacancy = value

    feedback = [
        apply
        for apply in job_response_storage.get_response()
        if apply.vacancy_id == vacancy_id
    ]
    context = {"title": "Vacancy", "vacancy": vacancy, "feedback": feedback}
    return render(request, "core/get_vacancy_core.html", context=context)


@require_http_methods(["GET", "POST"])
def add_vacancy_apply_core_controller(
    request: WSGIRequest, vacancy_id: int
) -> HttpResponse:
    if request.POST:
        vacancy_form = VacancyResponseForm(data=request.POST)
        if vacancy_form.is_valid():
            job_response = from_dict(JobResponseDTO, vacancy_form.cleaned_data)
            job_response.vacancy_id = vacancy_id
            job_response_storage.add_response(response=job_response)

    form = VacancyResponseForm()
    context = {"title": "Add apply to job", "form": form}
    return render(request, "core/add_vacancy_apply_core.html", context=context)


@require_http_methods(["GET"])
def get_company_core_controller(request: WSGIRequest, company_id: int) -> HttpResponse:
    for value in companies_storage.get_companies():
        if value.company_id == company_id:
            company = value

    feedback = [
        review
        for review in company_review_storage.get_response()
        if review.company_id == company_id
    ]
    context = {"title": "Company", "company": company, "feedback": feedback}
    return render(request, "core/get_company_core.html", context=context)


@require_http_methods(["GET", "POST"])
def add_review_company_core_controller(
    request: WSGIRequest, company_id: int
) -> HttpResponse:
    if request.POST:
        company_form = CompanyReviewForm(data=request.POST)
        if company_form.is_valid():
            review = from_dict(CompanyReviewDTO, company_form.cleaned_data)
            review.company_id = company_id
            company_review_storage.add_response(response=review)

    form = CompanyReviewForm()
    context = {"title": "Add review", "form": form}
    return render(request, "core/add_review_company_core.html", context=context)
