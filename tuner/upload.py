''' tuner/upload.py (S3에 업로드)
    로컬 모델을 S3에 업로드하는 함수
'''
import os
import boto3
from config import settings

def upload_to_s3(local_path, model_name):
    """
    로컬 모델을 S3에 업로드
    """
    bucket_name = settings.s3_bucket_name
    s3_path = f"{settings.s3_model_path}{model_name}.zip"

    if not bucket_name:
        print("S3_BUCKET_NAME is not set. Skipping upload.")
        return

    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key,
    )
    zip_path = f"{local_path}.zip"

    # 모델 디렉토리를 압축
    os.system(f"zip -r {zip_path} {local_path}")

    # S3에 업로드
    s3.upload_file(zip_path, bucket_name, s3_path)
    print(f"Model {model_name} uploaded to s3://{bucket_name}/{s3_path}")

    # 로컬 zip 파일 삭제
    os.remove(zip_path)