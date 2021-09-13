from sqlalchemy.orm import Session

from app.persistance.user_model import User
from app.util.utils import verify_password, get_password_hash


class UserRepository:
    def __init__(self, session: Session):
        self.__session = session

    def create_user(
            self,
            username: str = None,
            password: str = None,
            age: int = None,
            descriptions: str = None,
    ) -> bool:
        try:

            user_model = User(
                username=username,
                password=get_password_hash(password),
                age=age,
                descriptions=descriptions,
            )
            self.__session.add(user_model)
            self.__session.commit()
            return True
        except Exception as e:
            # self.__session.rollback()
            # self.__session.flush()
            # self.__logger.error(self,
            #     msg=f"[UserRepository][create user][Exception]error message:{e}"
            # )
            print(e)
            return False

    def get_user(
            self,
            username: str = None,
    ) -> bool:
        try:
            user_model = self.__session.query(User).filter(User.username == username).first()
            return user_model.to_entity()
        except Exception as e:

            return False

    def login_user(
            self,
            username: str = None,
            password: str = None,
    ) -> bool:
        try:
            user_model = self.__session.query(User).filter(User.username == username).first()

            # if user_model.password!=password:
            if not verify_password(password, user_model.password):
                return False
            return True
        except Exception as e:

            return False

    def delete_user(
            self,
            username: str = None,
            password: str = None,
    ) -> bool:
        try:
            user_model = self.__session.query(User).filter(User.username == username).first()
            if not verify_password(password, user_model.password):
                return False
            self.__session.delete(user_model)
            self.__session.commit()

            return True
        except Exception as e:

            return False

    def update_user(
            self,
            age: int = None,
            descriptions: str = None,
            username: str = None,
    ) -> bool:
        try:
            user_model = self.__session.query(User).filter(User.username == username).first()
            user_model.age = age
            user_model.descriptions = descriptions

            self.__session.add(user_model)
            self.__session.commit()

            return True
        except Exception as e:

            return False
