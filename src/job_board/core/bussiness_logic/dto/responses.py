from dataclasses import dataclass


@dataclass
class ResponsesDTO:
    user: str
    vacancy: str
    accompanying_text: str
    resume: str
    status: str
