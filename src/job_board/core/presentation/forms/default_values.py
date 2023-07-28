from core.models import (
    Competencies,
    EmploymentFormats,
    Genders,
    ResponseStatuses,
    Skills,
    UserStatuses,
)

USER_STATUS = [(status.status, status.status) for status in UserStatuses.objects.all()]

EMPLOYMENT_FORMATS = [
    (value.employment_format, value.employment_format)
    for value in EmploymentFormats.objects.all()
]

COMPETENCE = [
    (competence.competence, competence.competence)
    for competence in Competencies.objects.all()
]

SKILLS = [(skill.skill, skill.skill) for skill in Skills.objects.all()] + [("", "")]

GENDERS = [(gender.gender, gender.gender) for gender in Genders.objects.all()]

STATUS_JOBRESPONSE = [
    (status.status, status.status) for status in ResponseStatuses.objects.all()
]
