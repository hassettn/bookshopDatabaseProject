# bookshop_app/config.py

from pydantic import BaseSettings
from functools import lru_cache


# singular db contains all tables
# sqlalchemy allows us to interface with the sqlite database using python classes,
# and without using sql commands,
# but I can actually do sql commands
class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./bookshop.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
