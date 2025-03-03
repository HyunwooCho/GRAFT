# PyTorch가 포함된 Python 3.10 베이스 이미지 사용 (GPU 지원 가능)
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY requirements.txt .

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# LLM 다운로드 및 튜닝 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
