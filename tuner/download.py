''' tuner/download.py (모델 다운로드 스크립트)
    Hugging Face 모델 다운로드 함수
'''
import os
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import snapshot_download
from config import settings # 환경 변수에서 Huggingface 토큰, AWS 키 로딩
from upload import upload_to_s3

import warnings
warnings.simplefilter("ignore", FutureWarning)  # FutureWarning 숨기기

def download_model(model_name: str, save_dir: str = "models/"):
    """
    지정된 Hugging Face 모델을 다운로드하여 로컬 저장소에 저장
    백그라운드에서 실행되도록 설계
    
    Args:
        model_name (str): Hugging Face 모델 이름 (예: "bert-base-uncased")
        save_dir (str): 모델을 저장할 디렉토리 (기본값: "models/")
    
    Returns:
        str: 모델이 저장된 경로
    """
    os.makedirs(save_dir, exist_ok=True)

    print(f"Downloading {model_name} from Hugging Face...")
    # model_path = snapshot_download(
    #     repo_id=model_name,
    #     cache_dir=save_dir,
    #     token=settings.huggingface_token  # 환경 변수에서 HF 토큰 가져오기
    # )
    
    # print(f"Model downloaded to: {model_path}")
    try:
        model = AutoModel.from_pretrained(model_name, token=settings.huggingface_token)
        tokenizer = AutoTokenizer.from_pretrained(model_name, token=settings.huggingface_token)

        model_path = os.path.join(save_dir, model_name)
        os.makedirs(model_path, exist_ok=True)

        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)

        print(f"Model {model_name} successfully downloaded and saved at {model_path}")

        # S3에 업로드
        # upload_to_s3(model_path, model_name)
    except Exception as e:
        print(f"Download failed for {model_name}: {str(e)}")
    return model_path

if __name__ == "__main__":
    model_name = "bert-base-uncased"  # 테스트용 기본 모델
    download_model(model_name)
