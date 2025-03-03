''' api/services/tuner_client.py (api/ -> /tuner)
    api에서 tuner로 HTTP 요청 보내기
'''
import requests

TUNER_URL = "http://tuner:8001"  # docker-compose에서 서비스명으로 접근 가능

def download_model(model_name: str):
    response = requests.post(f"{TUNER_URL}/download", json={"model_name": model_name})
    return response.json()

def fine_tune_model(model_name: str, dataset_path: str):
    response = requests.post(f"{TUNER_URL}/train", json={"model_name": model_name, "dataset_path": dataset_path})
    return response.json()
