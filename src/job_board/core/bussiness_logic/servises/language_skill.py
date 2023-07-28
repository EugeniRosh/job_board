from __future__ import annotations

from core.models import Languages, LanguageSkills, Skills


def get_skill(skill: str) -> Skills:
    skill_from_db: tuple[Skills, bool] = Skills.objects.get_or_create(skill=skill)
    return skill_from_db[0]


def get_language(language: str) -> Languages:
    language_from_db: tuple[Languages, bool] = Languages.objects.get_or_create(
        title=language.lower()
    )
    return language_from_db[0]


def get_language_skill(language: str, skill: str) -> list[LanguageSkills]:
    language_from_db = get_language(language=language)
    skill_from_db = get_skill(skill=skill)

    language_from_db.skill.set([skill_from_db])

    language_skill = LanguageSkills.objects.get(
        language=language_from_db.id, skill=skill_from_db.id
    )

    return [language_skill]
