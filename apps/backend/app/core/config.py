from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки приложения"""
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "FoodFleet Backend"
    DEBUG: bool = True
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"
    DATABASE_NAME: str = "foodfleet"
    DATABASE_URI: str = ""

    @property
    def get_database_uri(self) -> str:
        """Получение URI базы данных"""
        if self.DATABASE_URI:
            return self.DATABASE_URI

        return f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        env_prefix="FOODFLEET_",
    )


settings = Settings()

settings.DATABASE_URI = settings.get_database_uri
