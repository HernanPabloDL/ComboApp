from dotenv import load_dotenv
import os
load_dotenv()

class Settings:
    PROJECT_NAME: str = "ComboBuilder API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./combobuilder.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

settings = Settings()