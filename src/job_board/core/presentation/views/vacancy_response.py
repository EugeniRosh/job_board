from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from core.presentation.forms import VacancyResponseForm
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.http.response import HttpResponse

logger = logging.getLogger(__name__)


@require_http_methods(["GET", "POST"])
def add_vacancy_apply_core_controller(
    request: WSGIRequest, vacancy_id: int
) -> HttpResponse:
    try:
        if request.POST:
            vacancy_form = VacancyResponseForm(data=request.POST)
            if vacancy_form.is_valid():
                ...
                logger.info("add new vacancy apply")

        form = VacancyResponseForm()
        context = {"title": "Add apply to job", "form": form}
        return render(request, "core/add_vacancy_apply_core.html", context=context)

    except Exception as err:
        logger.critical(err)
