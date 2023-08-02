from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from core.bussiness_logic.dto import EmployeeDTO
from core.bussiness_logic.servises import add_employee, get_employees_company
from core.presentation.forms import EmployeesForm
from dacite import from_dict

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.http.response import HttpResponse

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)


@require_http_methods(["GET", "POST"])
def add_employee_core_controller(request: WSGIRequest, company_id: int) -> HttpResponse:
    try:
        if request.POST:
            form_employee = EmployeesForm(data=request.POST, files=request.FILES)
            if form_employee.is_valid():
                employee = from_dict(EmployeeDTO, form_employee.cleaned_data)
                add_employee(data=employee, company_id=company_id)
                logger.info("add new employee")

        form = EmployeesForm()
        context = {"title": "Add employee", "form": form}
        return render(request, "core/add_employee_core.html", context=context)

    except Exception as err:
        logger.critical(err)


@require_http_methods(["GET"])
def employees_company_core_controller(
    request: WSGIRequest, companyname: str
) -> HttpResponse:
    try:
        employees = get_employees_company(company=companyname)
        logger.info("received by all employees of the company")
        context = {"title": "Employees company", "employees": employees}
        return render(request, "core/employees_company.html", context=context)

    except Exception as err:
        logger.critical(err)
