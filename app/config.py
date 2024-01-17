from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    github_client_id: str
    github_client_secret: str

    # Файл с чувствительными данными
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()