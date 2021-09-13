from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
from fastapi_login import LoginManager
from jose import JWTError, jwt
from passlib.context import CryptContext

from core.dto.user_dto import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET = "ddf4c664a5e4f143ada712ae692806f204c6a1c49bae8187def1dec01f2feff8"  # .env 에 아직 안넣었음 - 추후 secret manager 활용?
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
manager = LoginManager(SECRET, '/login/', use_cookie=True)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    return token_data.json()[14:-2]


def get_payload_from_token(header: str = Header(None)):
    try:
        token = header.split(" ")[-1]
        payload = header.get_payload(token)
        return payload["username"]
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_payload_from_token_test():
    return "Test_ID6"


def get_payload_from_token_test_wrong():
    return "wrong"
