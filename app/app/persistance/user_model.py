from sqlalchemy import Column, Integer, String

from app.database import Base
from core.entity.user_entity import UserEntity


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    username = Column(String, unique=True)
    age = Column(Integer)
    descriptions = Column(String, default="")

    def to_entity(self):
        return UserEntity(
            id=self.id,
            username=self.username,
            age=self.age,
            descriptions=self.descriptions,
        )
