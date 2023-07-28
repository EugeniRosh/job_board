from django.core.exceptions import ValidationError
from django.core.files import File


class ValidateFileExtension:
    def __init__(self, extensions: list[str]) -> None:
        self._extension = extensions

    def __call__(self, value: File) -> None:
        file_extension = value.name.split(".")[-1]
        if file_extension not in self._extension:
            raise ValidationError(message=f"Accept only {self._extension}")


class ValidatorFileSize:
    def __init__(self, max_size: int) -> None:
        self._max_size = max_size

    def __call__(self, value: File) -> None:
        if value.size > self._max_size:
            max_size_mb = self._max_size // 1_000_000
            raise ValidationError(message=f"Max size file must be {max_size_mb} MB")


class ValidatorMaxNumberValue:
    def __init__(self, max_count: int) -> None:
        self.max_count = max_count

    def __call__(self, value: str) -> None:
        if self.max_count < len(value.split("\r\n")):
            raise ValidationError(message=f"Max value must be {self.max_count}")
