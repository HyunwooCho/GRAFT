''' tuner/train.py (파인 튜닝 함수)
    파인 튜닝 함수
'''
import os
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset

def fine_tune_model(model_name: str, dataset_name: str, epochs: int, save_dir: str = "models/finetuned/"):
    """
    모델을 주어진 데이터셋으로 파인 튜닝하는 함수
    """
    os.makedirs(save_dir, exist_ok=True)
    
    print(f"🔹 Fine-tuning {model_name} with {dataset_name} for {epochs} epochs...")

    try:
        # 모델 및 토크나이저 불러오기
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # 데이터셋 로드
        dataset = load_dataset(dataset_name)

        # 학습 설정
        training_args = TrainingArguments(
            output_dir=os.path.join(save_dir, model_name),
            num_train_epochs=epochs,
            per_device_train_batch_size=8,
            save_strategy="epoch",
            logging_dir="./logs"
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"]
        )

        # 학습 시작
        trainer.train()
        
        print(f"Fine-tuning completed! Model saved at {os.path.join(save_dir, model_name)}")
    except Exception as e:
        print(f"Fine-tuning failed for {model_name}: {str(e)}")
