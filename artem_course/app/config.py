from typing import Literal

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_NAME: str
    TEST_DB_USER: str
    TEST_DB_PASS: str

    REDIS_CACHE_STR: str
    REDIS_CELERY_STR: str

    HASH_KEY: str
    HASH_ALGO: str

    ADMIN_SECURE_KEY: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
