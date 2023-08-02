from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from core.bussiness_logic.dto import SearchVacancyDTO, VacancyDTO
from core.bussiness_logic.exeptions import ValueNotExists
from core.bussiness_logic.servises import (
    add_vacancy,
    get_all_vacancy,
    get_vacancy_by_id,
)
from core.presentation.converters import converter_data_ftom_dto
from core.presentation.forms import SearchVacancyForm, VacancyForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.http.response import HttpResponse

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def index_controller(request: WSGIRequest) -> HttpResponse:
    try:
        form = SearchVacancyForm(data=request.GET)
        if form.is_valid():
            search_vacancy_filter: SearchVacancyDTO = converter_data_ftom_dto(
                SearchVacancyDTO, form.cleaned_data
            )
            vacancies = get_all_vacancy(search_filters=search_vacancy_filter)
            logger.info("received all vacancies")

            form = SearchVacancyForm()
            context = {"title": "JOB BOARD", "vacancies": vacancies, "form": form}
        else:
            context = {"title": "JOB BOARD", "form": form}

        return render(request, "core/index.html", context=context)

    except Exception as err:
        logger.critical(err)


@require_http_methods(["GET", "POST"])
def add_vacancy_core_controller(request: WSGIRequest, employee_id: int) -> HttpResponse:
    try:
        form = VacancyForm()

        if request.POST:
            form_vacancy = VacancyForm(data=request.POST)
            if form_vacancy.is_valid():
                vacancy = converter_data_ftom_dto(
                    dto=VacancyDTO, data=form_vacancy.cleaned_data
                )
                add_vacancy(data=vacancy, employee_id=employee_id)
                logger.info("add new vacancy")

        context = {"title": "Post a job", "form": form}
        return render(request, "core/add_vacancy_core.html", context=context)

    except Exception as err:
        logger.critical(err)


@require_http_methods(["GET"])
def get_vacancy_core_controller(request: WSGIRequest, vacancy_id: int) -> HttpResponse:
    try:
        try:
            vacancy, tags, vacancies = get_vacancy_by_id(vacancy_id=vacancy_id)
            logger.info(f"get vacancy: id = {vacancy_id}")
        except ValueNotExists:
            logger.error(f"non-existent vacancy requested id = {vacancy_id}")
            return HttpResponseRedirect(redirect_to=reverse("index"))

        feedback: list[str] = []

        context = {
            "title": "Vacancy",
            "vacancy": vacancy,
            "tags": tags,
            "vacancies": vacancies,
            "feedback": feedback,
        }
        return render(request, "core/get_vacancy_core.html", context=context)

    except Exception as err:
        logger.critical(err)
