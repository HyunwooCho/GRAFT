<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/HyunwooCho/GRAFT/main/docs/media/GRAFT_logo.png" width="200"></td>
    <td>
      <h3>GRAFT: Generative AI Refinement & Fine-Tuning Toolkit</h3>
      <p> GRAFT is a GenAIOps framework designed to graft and fine-tune Generative AI models for domain-specific applications, ensuring optimal performance and seamless deployment. </p>
    </td>
  </tr>
</table>


# GRAFT (Generative AI Refinement & Fine-Tuning Toolkit)

GRAFT is an open-source framework designed to streamline **LLM downloading, fine-tuning, and benchmarking** with support for **multi-GPU training and modular execution**.

## Meaning & Philosophy
- The term **"Graft"** symbolizes the **integration and adaptation of a powerful Generative AI model to specific domains**.  
- The **core goal** of the framework is to **preserve Generative AI’s strengths while enabling effortless domain-specific customization**.  

---

## Core Components of GRAFT

| Component | Description |
|-----------|------------|
| **G**enerative AI | **Utilizes pre-trained models as a foundation for domain adaptation** |
| **R**efinement | **Fine-tunes and optimizes AI models based on domain-specific data** |
| **A**daptation | **Customizes AI models according to user and business requirements** |
| **F**ine-Tuning | **Employs transfer learning and parameter tuning for enhanced performance** |
| **T**oolkit | **Provides MLOps tools for seamless model deployment, monitoring, and maintenance** |

---

## Key Goals of GRAFT  

1. **Domain-Specific Fine-Tuning**  
   - Adapts pre-trained Generative AI models to specific industries (e.g., healthcare, finance, gaming, design)  
   - Implements efficient training techniques (LoRA, QLoRA, PEFT)  

2. **Automated Optimization & Deployment**  
   - **CI/CD pipeline** for streamlined MLOps workflows  
   - **Automated hyperparameter tuning (AutoML)**  

3. **Efficient Model Training & Compression**  
   - Supports **model quantization and pruning** for reduced computational costs  
   - Optimized for both **cloud and on-premises** environments  

4. **Model Monitoring & Continuous Improvement**  
   - **Detects data drift** and automates model updates  
   - Provides **real-time performance monitoring & evaluation**  

---



## Main Features of GRAFT

- **Web App & Python Package Support** - Run as an API-powered web UI or via CLI
- **Selective LLM Model Download** - Choose and manage Hugging Face models
- **PEFT-based Fine-Tuning (LoRA, QLoRA)** - Efficient fine-tuning with reduced memory usage
- **Multi-GPU Training (PyTorch DDP)** - Optimized distributed training on a single node
- **Benchmarking & Visualization** - Monitor results with Vega-Lite dashboard

---

## 🏗️ Installation & Usage

### 1️⃣ Python Package Mode

#### 🔹 Install

```sh
pip install graft-ai
```

#### 🔹 CLI Execution

```sh
graft download --model llama-2-7b
graft train --model llama-2-7b --dataset dataset.json
graft benchmark --model llama-2-7b
```

#### 🔹 Python Code Usage

```python
from graft.core import ModelManager

manager = ModelManager()
model = manager.download("llama-2-7b")
manager.fine_tune(model, "dataset.json")
manager.benchmark(model)
```


### 2️⃣ Web App Mode

#### 🔹 Run with Docker

```sh
docker-compose up --build
```

#### 🔹 Access Web UI

```
http://localhost:3000
```

#### 🔹 API Endpoints (FastAPI)

| Method | Endpoint           | Description             |
| ------ | ------------------ | ----------------------- |
| `GET`  | `/models`          | List available models   |
| `POST` | `/models/download` | Download an LLM model   |
| `POST` | `/models/train`    | Fine-tune a model       |
| `GET`  | `/models/progress` | Check training progress |

---

## Technology Stack & Justification

| **Service**                     | **Technology Stack**          | **Justification**                                    |
| ------------------------------- | ----------------------------- | ---------------------------------------------------- |
| **API (Web Mode)**              | **FastAPI**                   | Provides API endpoints for model management          |
|                                 | **Celery**                    | Handles background tasks (fine-tuning, benchmarking) |
|                                 | **Redis**                     | Message broker for distributed task processing       |
| **Python Package (CLI/Script)** | **Hugging Face Transformers** | Handles LLM downloading and model loading            |
|                                 | **PEFT (LoRA, QLoRA)**        | Optimizes LLM fine-tuning with reduced memory usage  |
|                                 | **PyTorch (DDP)**             | Supports multi-GPU distributed training              |
|                                 | **BitsAndBytes**              | Supports quantization for memory efficiency          |
| **Frontend**                    | **Next.js (React)**           | Provides an interactive UI                           |
| **Database**                    | **PostgreSQL**                | Stores structured data related to LLM processing     |
| **Infrastructure**              | **Docker & Docker Compose**   | Supports microservices deployment                    |



---



## Supported PEFT & Memory Optimization Techniques Comparison

| Technique | Type | Purpose | Memory Savings | Speed Impact | Features |
|---|---|---|---|---|---|
| **LoRA (Low-Rank Adaptation)** | PEFT | Update only a subset of weights | 🔵🔵🔵🔵🟢 (Up to 90%) | ⬆️ Fast | Fine-tunes FFN & attention weights with minimal changes |
| **DoRA (Decoupled LoRA)** | PEFT | Improved LoRA (decouples FFN and MHA) | 🔵🔵🔵🟢🟢 (Up to 80%) | ⬆️ Fast | More precise fine-tuning than LoRA |
| **QLoRA (Quantized LoRA)** | PEFT + Quantization | 4-bit quantization + LoRA | 🔵🔵🔵🔵🔵 (Up to 95%) | ⬇️ Slightly slower | Enables training large models (33B+) on low-spec GPUs |
| **QDoRA (Quantized DoRA)** | PEFT + Quantization | Combination of QLoRA + DoRA | 🔵🔵🔵🔵🟢 (Up to 90%) | ⬇️ Slightly slower | Compresses LoRA & DoRA into 4-bit |
| **Adapters (Adapter-Tuning)** | PEFT | Train only specific layers | 🔵🔵🔵🟢🟢 (Up to 70%) | ⬆️ Fast | More versatile than LoRA, applicable to vision & NLP |
| **Prompt Tuning** | PEFT | Modify input prompts | 🔵🔵🔵🟢🟢 (Up to 70%) | ⬆️ Fast | Optimizes prompts without changing the model |
| **Prefix Tuning** | PEFT | Prompt + additional trainable vectors | 🔵🔵🟢🟢🟢 (Up to 60%) | ⬆️ Fast | Adjusts attention keys/values with minimal parameters |
| **P-Tuning (Prompt Tuning v2)** | PEFT | Improved Prefix Tuning | 🔵🔵🔵🟢🟢 (Up to 70%) | ⬆️ Fast | Applies to lower layers, effective in multilingual tasks |
| **ZeRO-1 (Zero Redundancy Optimizer)** | Memory Optimization | Distributes optimizer states | 🔵🔵🟢🟢🟢 (Up to 50%) | ⬆️ Fast | Useful in multi-GPU environments |
| **ZeRO-2** | Memory Optimization | Distributes optimizer + gradients | 🔵🔵🔵🟢🟢 (Up to 60%) | ⬆️ Fast | Further reduces memory usage |
| **ZeRO-3** | Memory Optimization | Distributes parameters as well | 🔵🔵🔵🔵🟢 (Up to 75%) | ⬇️ Slightly slower | Spreads entire model across multiple GPUs |
| **Offloading (CPU/NVMe Offload)** | Memory Optimization | Uses CPU/NVMe when GPU is limited | 🔵🔵🔵🟢🟢 (Up to 80%) | ⬇️ Slower | Enables LLM training on low-end GPUs |
| **Gradient Checkpointing** | Memory Optimization | Reduces activation memory | 🔵🔵🟢🟢🟢 (Up to 50%) | ⬇️ Slightly slower | Recomputes some activation values |

---

## Best Practices: Recommended Optimal Combinations

### RTX 3090/4090 (Below 24GB VRAM)
- **QLoRA + ZeRO-3 + CPU Offloading + Gradient Checkpointing** → **Supports models up to 13B**

### A100 40GB
- **LoRA + ZeRO-3 + Gradient Checkpointing** → **Supports models up to 30B**

### A100 80GB / H100
- **Full Fine-tuning + ZeRO-3 + Offloading** → **Supports models from 65B to 175B**

---

## Low-Cost Fine-Tuning Options
- **QLoRA / QDoRA + Gradient Checkpointing**
- **Prompt Tuning (Prompt Tuning, Prefix Tuning, P-Tuning)**

## Essential for Large Model Training
- **ZeRO-3 + Offloading + Gradient Checkpointing**


---



## 🎯 Roadmap

-

---

## 📜 License

GRAFT is released under the **MIT License**.

---

## 💡 Contributing

We welcome contributions! Please submit issues and pull requests on our [GitHub repository](https://github.com/HyunwooCho/graft).

---

## 📞 Contact

For questions and discussions, join our community on Discord or open an issue on GitHub.





