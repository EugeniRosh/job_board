from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from core.bussiness_logic.dto import CompanyDTO
from core.bussiness_logic.exeptions import CreateUniqueError, ValueNotExists
from core.bussiness_logic.servises import (
    add_company,
    get_all_company,
    get_company_by_id,
    get_company_review,
)
from core.presentation.converters import converter_data_ftom_dto
from core.presentation.forms import CompanyForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.http.response import HttpResponse


logger = logging.getLogger(__name__)


@require_http_methods(["GET", "POST"])
def companies_core_controller(request: WSGIRequest) -> HttpResponse:
    try:
        company_list = get_all_company()
        context = {"title": "Companies", "company_list": company_list}
        logger.info("received all companies")
        return render(request, "core/companies_core.html", context=context)

    except Exception as err:
        logger.critical(err)


@require_http_methods(["GET", "POST"])
def add_company_core_controller(request: WSGIRequest) -> HttpResponse:
    try:
        form = CompanyForm()

        if request.POST:
            form_company = CompanyForm(data=request.POST, files=request.FILES)
            if form_company.is_valid():
                company = converter_data_ftom_dto(
                    dto=CompanyDTO, data=form_company.cleaned_data
                )

                try:
                    add_company(company=company)
                    logger.info("add new company")
                except CreateUniqueError:
                    form = form_company
                    form.add_error("name", "Company already exists")
            else:
                form = form_company

        context = {"title": "Add Company", "form": form}
        return render(request, "core/add_company_core.html", context=context)

    except Exception as err:
        logger.critical(err)


@require_http_methods(["GET"])
def get_company_core_controller(request: WSGIRequest, company_id: int) -> HttpResponse:
    try:
        try:
            company, business_lines = get_company_by_id(company_id=company_id)
            logger.info(f"get company: id = {company_id}")
        except ValueNotExists:
            logger.error(f"non-existent company requested id = {company_id}")
            return HttpResponseRedirect(redirect_to=reverse("companies_core"))

        feedback = get_company_review(company_id=company_id)

        context = {
            "title": "Company",
            "company": company,
            "feedback": feedback,
            "business_lines": business_lines,
        }
        return render(request, "core/get_company_core.html", context=context)

    except Exception as err:
        logger.critical(err)
