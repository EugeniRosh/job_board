from __future__ import annotations

from typing import TYPE_CHECKING

from core.bussiness_logic.exeptions import CreateUniqueError
from core.models import (
    Competencies,
    EmploymentFormats,
    Genders,
    Profiles,
    Users,
    UserStatuses,
)
from django.db.utils import IntegrityError

from .cities import get_city
from .common import change_file_size, rename_in_uuid
from .countries import get_country
from .language_skill import get_language_skill
from .tags import get_tags
from .work_format import get_work_format

if TYPE_CHECKING:
    from core.bussiness_logic.dto import UserDTO


def add_user(user: UserDTO) -> None:
    gender = Genders.objects.get(gender=user.gender)
    country = get_country(request_country=user.country)
    city = get_city(request_city=user.city)
    work_format = get_work_format(request_work_format=user.work_format)
    competence = Competencies.objects.get(competence=user.competence)
    employment_formats = EmploymentFormats.objects.get(
        employment_format=user.design_format
    )
    status = UserStatuses.objects.get(status=user.status)
    tags = get_tags(respons_tags=user.tags)

    user.resume = rename_in_uuid(user.resume)

    user.photo = rename_in_uuid(user.photo)
    user.photo = change_file_size(user.photo)
    try:
        user_db = Users.objects.create(
            name=user.name,
            surname=user.surname,
            age=user.age,
            work_experience=user.work_experience,
            resume=user.resume,
            photo=user.photo,
            experience_description=user.experience_description,
            salary_min=user.min_salary,
            salary_max=user.max_salary,
            profile=Profiles.objects.create(
                email=user.email,
                phone=user.phone,
                linkedin=user.linkedin,
                github=user.github,
                password=user.password,
                login=user.login,
                country=country,
                city=city,
                gender=gender,
            ),
            work_format=work_format,
            competence=competence,
            employment_formats=employment_formats,
            status=status,
        )

        user_db.tag.set(tags)
        if user.language and user.language_skill:
            language_skill = get_language_skill(
                language=user.language, skill=user.language_skill
            )
            user_db.language.set(language_skill)

    except IntegrityError:
        raise CreateUniqueError

    return None


def get_all_user() -> list[Users]:
    users = Users.objects.select_related(
        "profile", "status", "employment_formats", "competence", "work_format"
    ).prefetch_related("tag", "language")

    return list(users)
