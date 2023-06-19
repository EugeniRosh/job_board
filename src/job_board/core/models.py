#from django.db import models
from __future__ import annotations
from dataclasses import dataclass


class VacanciesStorage:
    def __init__(self) -> None:
        self._storage = []
    
    def add_vacancies(self, vacancie: Vacancy) -> None:
        self._storage.append(vacancie)

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
