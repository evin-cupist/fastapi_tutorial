from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = ""
    ENV_STATE: str = "dev"

    class Config:
        env_file = '.env'
        env_file_encodings = "utf-8"


def get_settings():
    if Settings().ENV_STATE == 'dev':
        return Settings(_env_file='dev.env')
    else:
        return Settings(_env_file='test.env')


settings = get_settings()
