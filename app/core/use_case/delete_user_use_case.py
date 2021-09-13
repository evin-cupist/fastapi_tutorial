from sqlalchemy.orm import Session

from core.dto.user_dto import UserDeleteDto
from core.repository.user_repository import UserRepository
from core.use_case_output import Failure, Success
from core.use_case_output.failure_type import FailureType


class DeleteUserUseCase:
    def __init__(self, session: Session):
        self.__user_repo = UserRepository(session=session)

    def execute(self, dto: UserDeleteDto, token: str):
        if dto.username != token:
            return Failure(FailureType.AUTH_INVALID_ERROR)

        result = self.__user_repo.delete_user(
            username=dto.username,
            password=dto.password
        )

        if dto.username is None or dto.password is None:
            return Failure(FailureType.INPUT_PARAMETER_ERROR)

        if result is False:
            # self.__logger.warning(
            #     f"[CreateUserUseCase][execute][Fail] "
            #     f"username: {dto.username}"
            # )
            return Failure(FailureType.NOT_FOUND_ERROR)

        return Success()
