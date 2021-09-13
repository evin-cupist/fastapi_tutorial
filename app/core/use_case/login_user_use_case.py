from sqlalchemy.orm import Session

from core.dto.user_dto import UserLoginDto
from core.repository.user_repository import UserRepository
from core.use_case_output import Failure, Success
from core.use_case_output.failure_type import FailureType


class LoginUserUseCase:
    def __init__(self, session: Session):
        self.__user_repo = UserRepository(session=session)

    def execute(self, dto: UserLoginDto):
        result = self.__user_repo.login_user(
            username=dto.username,
            password=dto.password
        )

        if result is False:
            # self.__logger.warning(
            #     f"[CreateUserUseCase][execute][Fail] "
            #     f"username: {dto.username}"
            # )
            return Failure(FailureType.NOT_FOUND_ERROR)

        return Success()
