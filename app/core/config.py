from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Social-Media"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ENVIRONMENT: str

    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        orm_mode = True

settings = Settings()