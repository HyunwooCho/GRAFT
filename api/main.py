''' api/main.py (FastAPI 기본 서버)
    FastAPI 앱 생성, /healthcheck 엔드포인트 추가
'''
from fastapi import FastAPI
from routes import healthcheck, models, env

app = FastAPI(title="GRAFT API", version="1.0")

# 라우터 추가
app.include_router(healthcheck.router, prefix="/healthcheck", tags=["Health"])
app.include_router(models.router, prefix="/models", tags=["Models"])
app.include_router(env.router, prefix="/env", tags=["Enviroment"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
