from typing import Generic, TypeVar

from core.use_case_output.failure_type import FailureType

_ValueType = TypeVar("_ValueType", covariant=True)


class UseCaseOutput(Generic[_ValueType]):
    data: _ValueType

    def get_data(self) -> _ValueType:
        raise NotImplementedError

    def get_meta(self) -> dict:
        raise NotImplementedError

    def is_success(self) -> bool:
        raise NotImplementedError


class Success(UseCaseOutput[_ValueType]):
    def __init__(self, data: _ValueType = None, meta: dict = None) -> None:
        self.data = data
        self.meta = {} if meta is None else meta

    def is_success(self) -> bool:
        return True

    def get_meta(self) -> dict:
        return self.meta

    def get_data(self) -> _ValueType:
        if self.data or isinstance(self.data, list) or isinstance(self.data, int):
            return self.data
        return {}


class Failure(UseCaseOutput[_ValueType]):
    def __init__(self, type_: FailureType, description: str = "") -> None:
        self.type = type_
        self.description = description

    def is_success(self) -> bool:
        return False

    def get_meta(self) -> dict:
        return {}

    def get_data(self) -> _ValueType:
        raise NotImplementedError

    def get_type(self) -> FailureType:
        return self.type

    def get_description(self) -> str:
        return self.description
