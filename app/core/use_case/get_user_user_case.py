from sqlalchemy.orm import Session

from core.dto.user_dto import UserGetDto
from core.repository.user_repository import UserRepository
from core.use_case_output import Failure, Success
from core.use_case_output.failure_type import FailureType


class GetUserUseCase:
    def __init__(self, session: Session):
        self.__user_repo = UserRepository(session=session)

    def execute(self, dto: UserGetDto):
        result = self.__user_repo.get_user(
            username=dto.username,
        )

        if dto.username is None:
            return Failure(FailureType.INPUT_PARAMETER_ERROR)

        if result is False:
            # self.__logger.warning(
            #     f"[CreateUserUseCase][execute][Fail] "
            #     f"username: {dto.username}"
            # )
            return Failure(FailureType.NOT_FOUND_ERROR)

        return Success(data=result)
