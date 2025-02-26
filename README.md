<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/HyunwooCho/GRAFT/main/docs/media/GRAFT_logo.png" width="200"></td>
    <td>
      <h3>GRAFT: Generative AI Refinement & Fine-Tuning Toolkit</h3>
      <p> GRAFT is a GenAIOps framework designed to graft and fine-tune Generative AI models for domain-specific applications, ensuring optimal performance and seamless deployment. </p>
    </td>
  </tr>
</table>


# GRAFT Framework  

GRAFT is a Generative AI fine-tuning and deployment framework.  

## 🔹 **Meaning & Philosophy**  
- The term **"Graft"** symbolizes the **integration and adaptation of a powerful Generative AI model to specific domains**.  
- The **core goal** of the framework is to **preserve Generative AI’s strengths while enabling effortless domain-specific customization**.  

---

## **🔧 Core Components of GRAFT**  

| Component | Description |
|-----------|------------|
| **G**enerative AI | **Utilizes pre-trained models as a foundation for domain adaptation** |
| **R**efinement | **Fine-tunes and optimizes AI models based on domain-specific data** |
| **A**daptation | **Customizes AI models according to user and business requirements** |
| **F**ine-Tuning | **Employs transfer learning and parameter tuning for enhanced performance** |
| **T**oolkit | **Provides MLOps tools for seamless model deployment, monitoring, and maintenance** |

---

## **🛠 Key Features of GRAFT**  

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

## **🚀 Use Cases for GRAFT**  

| Domain | Application |
|--------|------------|
| **Healthcare** | AI-driven medical document generation & patient data adaptation |
| **Coding** | AI-powered code completion, debugging assistance, and repository-based fine-tuning |
| **Smart Home** | AI-driven home automation, personalized voice assistants, and energy optimization |
| **Academic Research** | AI-assisted literature review & and scientific data analysis |
| **Design** | Brand-specific fine-tuning for text-to-image models |

---

## **🌟 Advantages of GRAFT**  
✅ **Fast & Efficient Fine-Tuning** – Quickly adapts AI models to new domains  
✅ **Flexible MLOps Support** – Compatible with on-premises, cloud, and hybrid environments  
✅ **Optimized Performance & Cost Reduction** – Implements quantization & intelligent model refinement  
✅ **Scalability & Integration** – API-based architecture for seamless service integration  

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
| **Offloading (CPU/NVMe Offload)** | Memory Optimization | Uses CPU/NVMe when GPU is limited | 🔵🔵🔵🔵🔵 (Up to 80%) | ⬇️ Slower | Enables LLM training on low-end GPUs |
| **Gradient Checkpointing** | Memory Optimization | Reduces activation memory | 🔵🔵🔵🟢🟢 (Up to 50%) | ⬇️ Slightly slower | Recomputes some activation values |

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



