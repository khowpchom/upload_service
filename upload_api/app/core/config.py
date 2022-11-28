from pydantic import BaseSettings


class Settings(BaseSettings):
    API_URL: str = "/v1"
    REDIS_URL: str = "redis://redis:6379/0"

    class Config:
        env_file = ".env"


settings = Settings()
