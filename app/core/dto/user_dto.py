from pydantic import BaseModel
from typing import Optional


class UserCreateDto(BaseModel):
    username: str = None
    password: str = None
    age: int = None
    descriptions: str = None


class UserUpdateDto(BaseModel):
    age: int = None
    descriptions: str = None

    def toJSON(self):
        return {
            "age": self.age,
            "descriptions": self.descriptions,
        }


class UserDeleteDto(BaseModel):
    username: str = None
    password: str = None


class UserDeleteIdDto(BaseModel):
    id: int = None
    password: str = None


class UserGetDtoID(BaseModel):
    id: int = None


class UserGetDto(BaseModel):
    username: str = None


class UserLoginDto(BaseModel):
    username: str = None
    password: str = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
