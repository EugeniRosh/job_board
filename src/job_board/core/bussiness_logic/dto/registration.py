from dataclasses import dataclass


@dataclass
class RegistrationDTO:
    login: str
    email: str
    password: str
    role: str
