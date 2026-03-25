# 🧠 Brain CT Hemorrhage Analysis (Segmentation + Classification)

## 🚀 Project Vision

This project aims to develop an AI-based system for **intracranial hemorrhage (ICH) analysis** from computed tomography (CT) scans.

The system is designed as a **modular pipeline**, combining computer vision and (future) language models to assist in medical image interpretation.

The final objective is to build a **deployable decision-support prototype** that integrates:

* Deep learning for hemorrhage detection and segmentation
* Structured feature extraction from imaging outputs
* Retrieval-Augmented Generation (RAG) for medical knowledge integration
* Large Language Models (LLMs) for human-readable explanations

---

## 🧩 System Architecture (High-Level)

```text
3D CT Scan (NIfTI)
        ↓
2D Slice Extraction
        ↓
Computer Vision Models
   ├── Classification (Hemorrhage / No Hemorrhage)
   └── Segmentation (Pixel-wise Mask)
        ↓
Structured Output (Future)
        ↓
LLM + RAG (Future)
        ↓
Clinical-style Explanation (Future)
```

---

## 🎯 Objectives

* Detect the presence of intracranial hemorrhage from CT scans
* Segment hemorrhage regions at the pixel level
* Build a scalable pipeline from **2D slice-based models → 3D volumetric models**
* Prepare outputs for integration with LLM + RAG systems

---

## 📊 Dataset

This project uses the dataset:

**Computed Tomography Images for Intracranial Hemorrhage Detection and Segmentation (v1.3.1)**
🔗 https://physionet.org/content/ct-ich/1.3.1/

* Contains CT scans of traumatic brain injury patients
* Includes expert-annotated hemorrhage regions
* Data provided in **3D NIfTI format**

> ⚠️ Please follow PhysioNet licensing and usage requirements.

---

## 🧠 Why Convert 3D CT to 2D?

CT scans are inherently **3D volumetric data**.

In this project, volumes are initially decomposed into **2D slices** to:

* Reduce computational complexity
* Enable faster experimentation and iteration
* Build strong baseline models
* Simplify debugging and visualization

This is a **deliberate engineering step**, not a limitation.

➡️ The pipeline will later be extended to full **3D modeling**.

---

## ⚙️ Pipeline Overview

1. Load 3D CT scans (NIfTI format)
2. Convert volumes into 2D slices
3. Preprocess images (normalization, resizing, filtering)
4. Train models:

   * Classification (hemorrhage detection)
   * Segmentation (pixel-wise mask prediction)
5. Evaluate performance using appropriate metrics

---

## 📥 Input / Output

### Input

* 2D CT slices extracted from 3D volumes

### Output

* **Classification**: Hemorrhage / No Hemorrhage
* **Segmentation**: Binary mask of hemorrhage regions

---

## 📈 Evaluation Metrics

* Classification:

  * Accuracy
  * Precision / Recall / F1-score

* Segmentation:

  * Dice Coefficient
  * Intersection over Union (IoU)

---

## 📌 Current Status

* [x] Dataset acquisition (PhysioNet CT-ICH)
* [x] 3D → 2D slice conversion
* [ ] 2D classification model
* [ ] 2D segmentation model
* [ ] Evaluation and benchmarking
* [ ] 3D volumetric modeling
* [ ] Structured feature extraction
* [ ] LLM + RAG integration
* [ ] Deployment (API + UI)

---

## 🔮 Future Work

### 🔹 Computer Vision

* Transition from 2D slice-based models to **3D CNN architectures**
* Improve segmentation accuracy using advanced models (e.g., U-Net variants, nnU-Net)

### 🔹 Multimodal AI Integration

* Convert CV outputs into **structured medical features**
* Integrate with **Retrieval-Augmented Generation (RAG)**
* Use LLMs to generate **human-readable explanations**

### 🔹 Deployment

* Build API (FastAPI / Flask)
* Develop user interface (Streamlit or web app)
* Containerize with Docker for production

---

## ⚠️ Disclaimer

This project is a **research and engineering prototype**.

It is **not intended for medical diagnosis or clinical use**.
The system is designed as a **decision-support and educational tool only**.

---

## 🤝 Team Structure

This project is part of a **modular AI system** developed by a team:

* **Computer Vision Module (this repository)**

  * Hemorrhage detection and segmentation

* **LLM + RAG Module (separate repository)**

  * Knowledge retrieval and explanation generation

Integration will be performed via APIs.

---

## 🧠 Key Focus

This project emphasizes:

* Medical image understanding
* Structured AI pipelines
* Transition from 2D → 3D modeling
* Real-world system design (not just model training)

---

## 📬 Contact

**Seyed Ali Rashidi (Farid)**
📧 [farid.rash@gmail.com](mailto:farid.rash@gmail.com)

---

⭐ If you find this project useful, consider giving it a star!
