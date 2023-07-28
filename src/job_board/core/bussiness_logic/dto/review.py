from dataclasses import dataclass


@dataclass
class CompanyReviewDTO:
    review_id: int | None
    user: str
    company_id: int | None
    review: str
    likes: int
    dislikes: int
