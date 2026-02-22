from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App
    app_name: str = "Code Review API"
    app_version: str = "0.1.0"
    debug: bool = False

    # OpenAI
    groq_api_key: str = ""

    # Redis
    redis_url: str = "redis://localhost:6379"

    # PostgreSQL
    database_url: str

    # GitHub Webhook
    github_webhook_secret: str = ""
    github_token: str = ""

    # Rate Limiting
    rate_limit: str = "10/minute"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()