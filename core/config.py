from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

class DatabaseConfig(BaseConfig):
    db_url: str

class AppConfig(BaseConfig):
    app_name: str = "Base CRUD app"
    app_version: str = "0.0.1"
    log_level: str = "INFO"
    allowed_origins: str = "http://localhost:8080,http://127.0.0.1:8080"
    receipt_analyzer_url: str = "http://receipt-api:8000"
    receipt_analyzer_internal_token: str = "development-only-change-me"
    receipt_analyzer_timeout_seconds: float = 5.0

    @property
    def cors_origins(self) -> list[str]:
        return [item.strip() for item in self.allowed_origins.split(",") if item.strip()]

database_config = DatabaseConfig()
app_config = AppConfig()