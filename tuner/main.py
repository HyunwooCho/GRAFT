''' tuner/main.py (자체 FastAPI 서버)
    api/와 통신하는 마이크로서비스 구조
'''
from fastapi import FastAPI
from pydantic import BaseModel
from download import download_model
from train import fine_tune_model

app = FastAPI()

# ✅ 요청 데이터 스키마 정의 (Pydantic 모델)
class DownloadRequest(BaseModel):
    model_name: str

class TrainRequest(BaseModel):
    model_name: str
    dataset_path: str
    epochs: int

@app.post("/download")
async def download_model_api(request: DownloadRequest):
    return download_model(request.model_name)

@app.post("/train")
async def fine_tune_api(request: TrainRequest):
    return fine_tune_model(request.model_name, request.dataset_path, request.epochs)

