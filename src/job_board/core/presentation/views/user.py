from __future__ import annotations

from typing import TYPE_CHECKING

from core.bussiness_logic.dto import UserDTO
from core.bussiness_logic.exeptions import CreateUniqueError
from core.bussiness_logic.servises import add_user, get_all_user
from core.presentation.converters import converter_data_ftom_dto
from core.presentation.forms import UserForm
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.core.handlers.wsgi import WSGIRequest
    from django.http.response import HttpResponse


@require_http_methods(["GET"])
def users_profile_core_controller(request: WSGIRequest) -> HttpResponse:
    users = get_all_user()
    context = {"title": "Users profile", "users": users}
    return render(request, "core/user_profile_core.html", context=context)


@require_http_methods(["GET", "POST"])
def add_users_profile_core_controller(request: WSGIRequest) -> HttpResponse:
    form = UserForm()

    if request.POST:
        form_user = UserForm(data=request.POST, files=request.FILES)
        if form_user.is_valid():
            user = converter_data_ftom_dto(dto=UserDTO, data=form_user.cleaned_data)
            try:
                add_user(user=user)
            except CreateUniqueError:
                form = form_user
                form.add_error("login", "Login already exists")

    context = {"title": "Add users profile", "form": form}
    return render(request, "core/add_user_profile_core.html", context=context)
