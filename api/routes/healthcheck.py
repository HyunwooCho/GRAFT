''' api/routes/healthcheck.py (서버 상태 확인 API)
    /healthcheck 엔드포인트를 통해 서버가 정상 작동하는 지 확인
'''
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def health_check():
    """
    FastAPI 서버가 정상 동작하는지 확인하는 API
    """
    return {"status": "ok", "message": "GRAFT API is running"}
