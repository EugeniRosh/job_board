from __future__ import annotations

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

require_http_methods(["GET", "POST"])


def add_employee_core_controller(request: WSGIRequest, company_id: int) -> HttpResponse:
    if request.POST:
        form_employee = EmployeesForm(data=request.POST, files=request.FILES)
        if form_employee.is_valid():
            employee = from_dict(EmployeeDTO, form_employee.cleaned_data)
            add_employee(data=employee, company_id=company_id)

    form = EmployeesForm()
    context = {"title": "Add employee", "form": form}
    return render(request, "core/add_employee_core.html", context=context)


require_http_methods(["GET"])


def employees_company_core_controller(
    request: WSGIRequest, companyname: str
) -> HttpResponse:
    employees = get_employees_company(company=companyname)
    context = {"title": "Employees company", "employees": employees}
    return render(request, "core/employees_company.html", context=context)
