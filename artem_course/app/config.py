from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    REDIS_CACHE_STR: str
    REDIS_CELERY_STR: str

    HASH_KEY: str
    HASH_ALGO: str

    ADMIN_SECURE_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
