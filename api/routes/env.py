''' api/routes/env (환경 변수 확인 API)
    환경 변수 확인 API 엔드포인트
'''
from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/env")
def get_env():
    """
    .env 환경 변수 확인 API
    """
    return {
        "HUGGINGFACE_TOKEN": os.getenv("HUGGINGFACE_TOKEN"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID"),
        "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "S3_BUCKET_NAME": os.getenv("S3_BUCKET_NAME"),
        "S3_MODEL_PATH": os.getenv("S3_MODEL_PATH"),        
    }
