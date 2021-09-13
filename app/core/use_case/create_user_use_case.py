from sqlalchemy.orm import Session

from core.dto.user_dto import UserCreateDto
from core.repository.user_repository import UserRepository
from core.use_case_output import Failure, Success
from core.use_case_output.failure_type import FailureType

class CreateUserUseCase:
    def __init__(self, session: Session):
        self.__user_repo = UserRepository(session=session)

    def execute(self, dto: UserCreateDto):
        ##usercheck

        ##create
        result = self.__user_repo.create_user(
            username=dto.username,
            password=dto.password,
            age=dto.age,
            descriptions=dto.descriptions,
        )

        if dto.username is None or dto.password is None or dto.age is None:
            return Failure(FailureType.INPUT_PARAMETER_ERROR)

        if result is False:
            # self.__logger.warning(
            #     f"[CreateUserUseCase][execute][Fail] "
            #     f"username: {dto.username}"
            # )
            return Failure(FailureType.GENERATE_DATA_ERROR)

        return Success(data=dto)
