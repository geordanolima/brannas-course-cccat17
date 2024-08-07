import re

from src.presenter import ErrorInvalidEmail

from ._base_value_object import BaseValueObject


class EmailObject(BaseValueObject):
    def __init__(self, value: str) -> None:
        if not self._validate(value=value):
            raise ErrorInvalidEmail()
        self._value = value

    def _validate(self, value: str) -> bool:
        return re.search(r"^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z0-9]+(\.[a-zA-Z]{2,})+$", value)
