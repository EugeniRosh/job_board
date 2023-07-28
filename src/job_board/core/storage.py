from __future__ import annotations

from core.bussiness_logic.dto import CompanyReviewDTO, ResponsesDTO


class JobResponseStorage:
    def __init__(self) -> None:
        self._response_id = 1
        self._storage: list[ResponsesDTO] = []

    def add_response(self, response: ResponsesDTO) -> None:
        self._response_id += 1
        self._storage.append(response)

    def get_response(self) -> list[ResponsesDTO]:
        return self._storage


class CompanyReviewStorage:
    def __init__(self) -> None:
        self._response_id = 1
        self._storage: list[CompanyReviewDTO] = []

    def add_response(self, response: CompanyReviewDTO) -> None:
        response.review_id = self._response_id
        self._response_id += 1
        self._storage.append(response)

    def get_response(self) -> list[CompanyReviewDTO]:
        return self._storage


job_response_storage = JobResponseStorage()
company_review_storage = CompanyReviewStorage()
