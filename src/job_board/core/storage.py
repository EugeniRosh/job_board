from __future__ import annotations

from dataclasses import dataclass


class VacanciesStorage:
    def __init__(self) -> None:
        self._storage: list[Vacancy] = []

    def add_vacancies(self, vacancy: Vacancy) -> None:
        self._storage.append(vacancy)

    def get_vacancies(self) -> list[Vacancy]:
        return self._storage


@dataclass
class Vacancy:
    title: str
    company: str
    competence: str
    experience: str
    min_salary: int
    max_salary: int


@dataclass
class VacancyCount:
    company: str
    count_vacancy: int


vacancies = VacanciesStorage()
