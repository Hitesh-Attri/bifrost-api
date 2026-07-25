from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "bifrost-api"
    app_env: str = "development"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 80
    log_level: str = "info"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
