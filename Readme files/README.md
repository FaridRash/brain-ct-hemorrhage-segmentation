# 🧠 Brain CT Hemorrhage Analysis (Segmentation + Classification)

## 🚀 Project Vision

This project aims to develop an AI-based system for intracranial hemorrhage (ICH) analysis from computed tomography (CT) scans.

**Architecture:**
- Modular pipeline combining computer vision and future language models

**Long-term Goal:**
- Deployable decision-support prototype

**Components:**
- Deep learning for hemorrhage detection and segmentation
- Structured feature extraction
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs) for explanation

## 📌 Current Focus

**Version:** v1

Build a clean, reliable preprocessing pipeline and prepare a high-quality dataset

- Convert 3D CT volumes into 2D slices
- Preserve Hounsfield Units (HU)
- Create classification-ready dataset

## 🧩 System Architecture

3D CT Scan (NIfTI)
↓
2D Slice Extraction
↓
Preprocessing Pipeline
↓
Structured Dataset (Train / Val / Test)
↓
Deep Learning Models (Next Step)
↓

## 📊 Dataset

**Computed Tomography Images for Intracranial Hemorrhage Detection and Segmentation (v1.3.1)**

https://physionet.org/content/ct-ich/1.3.1/

- CT scans of traumatic brain injury patients
- Expert-annotated hemorrhage masks
- 3D NIfTI format (.nii)

⚠️ Follow PhysioNet licensing and usage requirements

## ⚙️ Implemented Pipeline

### Conversion
- Converted CT volumes into slice-wise 2D data
- CT slices
- Corresponding mask slices

### Data Format
- Removed: PNG
- Used: .npy
- Reason: Loss of medical precision
- Preserves Hounsfield Units (HU)
- Supports correct windowing and filtering

### Labeling
- Method: Segmentation to binary classification
- Logic: `label = 1 if any(mask == 255) else 0`
- Output: labels.csv

### Preprocessing
- Filtering (HU-based, partially implemented)
- Windowing (WL=40, WW=80)
- Normalization

⚠️ Filtering must be applied before windowing

### Dataset Split
- Method: 3D volume-level split
- Reason: Prevent data leakage
- Train: 2281
- Val: 241
- Test: 292

### Data Structure
processed_data/
  train/
    - images
    - labels.csv
  val/
    - images
    - labels.csv
  test/
    - images
    - labels.csv

### Validation
- Mask values verified as [0, 255]
- CT-mask alignment checked
- File/path issues resolved
- Pipeline rebuilt cleanly

## 📥 Input / Output

**Input:** 2D CT slices (.npy)

**Output:**
- Classification labels (0 / 1)
- Segmentation masks (binary)

## 📈 Evaluation Metrics

### Classification
- Accuracy
- Precision
- Recall
- F1-score

### Segmentation
- Dice Coefficient
- Intersection over Union (IoU)

## 📌 Current Status

### Completed
- Dataset acquisition
- 3D → 2D conversion
- Label generation
- Preprocessing pipeline design
- Dataset splitting
- Data validation

### Next Steps
- Train classification model
- Train segmentation model
- Evaluate models
- Move to 3D modeling
- Structured feature extraction
- LLM + RAG integration
- Deployment (API + UI)

## 🔮 Future Work

### computer_vision
### multimodal_ai
### deployment
- FastAPI / Flask
- Streamlit UI
- Docker

## 🤝 Team Structure

- **Computer Vision Module**: Detection and segmentation pipeline
- **LLM + RAG Module**: Explanation and knowledge integration

## 🧠 Key Focus

- HU-aware preprocessing
- Structured AI pipelines
- Data-centric development
- 2D to 3D transition

## ⚠️ Disclaimer

This project is a research and engineering prototype and not intended for clinical use

## 📬 Contact

If you find this project useful, consider giving it a star
