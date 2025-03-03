''' api/models/model.py (Pydantic 데이터 모델)
    API 요청의 데이터 구조(스키마)를 정의
'''
from pydantic import BaseModel

class ModelDownloadRequest(BaseModel):
    model_name: str # e.g., "meta-llama/Llama-2-7b-hf"
    # source: str = "huggingface"

class ModelTrainRequest(BaseModel):
    model_name: str
    dataset_name: str = "imdb"
    epochs: int = 3  # 기본값 3