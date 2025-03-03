''' tuner/config.py (Pydantic 셋팅)
    환경 변수(.env) 로딩
'''
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    huggingface_token: str
    database_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    s3_bucket_name: str
    s3_model_path: str = "models/"

    model_config = SettingsConfigDict(env_file=os.path.abspath(os.path.join(os.path.dirname(__file__), "../.env")),
                                      env_file_encoding="utf-8")

settings = Settings()

