''' api/routes/models.py (LLM 모델 관련 API)
    LLM 다운로드 및 튜닝을 처리하는 API 엔드포인트
'''
from fastapi import APIRouter, HTTPException, BackgroundTasks
from models.model import ModelDownloadRequest, ModelTrainRequest
from services.tuner_client import download_model, fine_tune_model

router = APIRouter()

@router.post("/download")
async def download_model_api(request: ModelDownloadRequest, background_tasks: BackgroundTasks):
    """
    Hugging Face에서 LLM을 다운로드하는 API 엔드포인트 (백그라운드 실행)
    """
    try:
        background_tasks.add_task(download_model, request.model_name)  # 백그라운드에서 실행
        return {"message": f"Downloading model {request.model_name} in the background."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")

@router.post("/train")
async def train_model_api(request: ModelTrainRequest, background_tasks: BackgroundTasks):
    """
    Fine-tuning API 엔드포인트 (백그라운드 실행)
    """
    try:
        background_tasks.add_task(fine_tune_model, request.model_name, request.dataset_name, request.epochs)
        return {"message": f"Fine-tuning model {request.model_name} with {request.dataset_name} in the background."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fine-tuning failed: {str(e)}")