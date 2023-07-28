from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import Reviews

if TYPE_CHECKING:
    from core.bussiness_logic.dto import CompanyReviewDTO


def add_review(review: CompanyReviewDTO, company_id: int) -> None:
    Reviews.objects.create(
        user=review.user,
        company_id=company_id,
        review=review.review,
        likes=review.likes,
        dislikes=review.dislikes,
    )
    return None


def get_company_review(company_id: int) -> list[Reviews | None]:
    try:
        review = (
            Reviews.objects.select_related("company")
            .get(company=company_id)
            .values("id", "user", "company__name", "review", "likes", "dislikes")
        )
    except Reviews.DoesNotExist:
        review = []

    return list(review)
