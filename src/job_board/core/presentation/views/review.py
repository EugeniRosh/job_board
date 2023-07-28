from __future__ import annotations

from typing import TYPE_CHECKING

from core.bussiness_logic.dto import CompanyReviewDTO
from core.bussiness_logic.servises import add_review
from core.presentation.converters import converter_data_ftom_dto
from core.presentation.forms import CompanyReviewForm
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.http.response import HttpResponse


@require_http_methods(["GET", "POST"])
def add_review_company_core_controller(
    request: WSGIRequest, company_id: int
) -> HttpResponse:
    if request.POST:
        company_form = CompanyReviewForm(data=request.POST)
        if company_form.is_valid():
            review = converter_data_ftom_dto(
                dto=CompanyReviewDTO, data=company_form.cleaned_data
            )
            add_review(review=review, company_id=company_id)

    form = CompanyReviewForm()
    context = {"title": "Add review", "form": form}
    return render(request, "core/add_review_company_core.html", context=context)
