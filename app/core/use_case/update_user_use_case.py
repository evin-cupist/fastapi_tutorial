from sqlalchemy.orm import Session

from core.dto.user_dto import UserUpdateDto
from core.repository.user_repository import UserRepository
from core.use_case_output import Failure, Success
from core.use_case_output.failure_type import FailureType


class UpdateUserUseCase:
    def __init__(self, session: Session):
        self.__user_repo = UserRepository(session=session)

    def execute(self, dto: UserUpdateDto, username: str):
        ##usercheck
        usercheck = self.__user_repo.get_user(
            username=username
        )
        if usercheck is False:
            return Failure(FailureType.NOT_AUTHORIZED_ERROR)
        ##create
        result = self.__user_repo.update_user(
            age=dto.age,
            descriptions=dto.descriptions,
            username=username
        )

        if result is False:
            # self.__logger.warning(
            #     f"[CreateUserUseCase][execute][Fail] "
            #     f"username: {dto.username}"
            # )
            return Failure(FailureType.INPUT_PARAMETER_ERROR)

        return Success(data=dto)
