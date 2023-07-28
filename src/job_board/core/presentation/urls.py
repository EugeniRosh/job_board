from core.presentation.views import (
    add_company_core_controller,
    add_employee_core_controller,
    add_review_company_core_controller,
    add_users_profile_core_controller,
    add_vacancy_apply_core_controller,
    add_vacancy_core_controller,
    companies_core_controller,
    employees_company_core_controller,
    get_company_core_controller,
    get_vacancy_core_controller,
    index_controller,
    users_profile_core_controller,
)
from django.urls import include, path

vacancy_patterns = [
    path("add/<int:employee_id>", add_vacancy_core_controller, name="add_vacancy_core"),
    path("<int:vacancy_id>/", get_vacancy_core_controller, name="get_vacancy_core"),
    path(
        "<int:vacancy_id>/apply/",
        add_vacancy_apply_core_controller,
        name="add_vacancy_apply_core",
    ),
]

company_patterns = [
    path("", companies_core_controller, name="companies_core"),
    path("add/", add_company_core_controller, name="add_company_core"),
    path("<int:company_id>/", get_company_core_controller, name="get_company_core"),
    path(
        "<int:company_id>/review",
        add_review_company_core_controller,
        name="add_review_company_core",
    ),
]

users_patterns = [
    path("", users_profile_core_controller, name="profile_core"),
    path("add/", add_users_profile_core_controller, name="add_profile_core"),
]

employees = [
    path(
        "<companyname>/",
        employees_company_core_controller,
        name="employees_company_core",
    ),
    path("<int:company_id>/", add_employee_core_controller, name="add_employee_core"),
]

urlpatterns = [
    path("", index_controller, name="index"),
    path("vacancy/", include(vacancy_patterns)),
    path("company/", include(company_patterns)),
    path("profile/", include(users_patterns)),
    path("employee/", include(employees)),
]
