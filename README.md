# 🧠 Brain CT Hemorrhage Analysis (Segmentation + Classification)

##  Project Vision

This project develops a **modular AI system** for intracranial hemorrhage (ICH) analysis from CT scans.

The system combines:
- **Computer Vision (CV)** → detection & segmentation  
- **Machine Learning (ML)** → decision making  
- **LLM + RAG (future)** → clinical-style explanations  

 **Goal:**  
Build a **deployable decision-support prototype** for fast and reliable hemorrhage detection.

---

##  System Overview

The pipeline follows a **data-centric and modular architecture**:

3D CT Scan (NIfTI)
↓
2D Slice Extraction
↓
Preprocessing Pipeline
↓
Structured Dataset (Train / Val / Test)
↓
Deep Learning Models (Segmentation + Classification)
↓
(Next) LLM + RAG + UI


---

##  Computer Vision Workflow

![CV Workflow](https://github.com/FaridRash/brain-ct-hemorrhage-segmentation/blob/main/Diagrams/CV%20Workflow.jpg)

This workflow describes the **inference-time pipeline** after model training:
- Input CT slice
- Preprocessing (cropping, filtering, windowing)
- Segmentation (U-Net)
- Classification decision (hemorrhage / no hemorrhage)

---

##  Training Workflow

![Training Workflow](https://github.com/FaridRash/brain-ct-hemorrhage-segmentation/blob/main/Diagrams/The%20Training%20Workflow.jpg)

This workflow describes how the model is trained:
- Dataset input
- Forward pass through segmentation model
- Loss computation
- Backpropagation
- Weight update via optimizer

---

##  Dataset

**Source:**  
PhysioNet – *CT Images for Intracranial Hemorrhage Detection and Segmentation (v1.3.1)*  
https://physionet.org/content/ct-ich/1.3.1/

### Characteristics
- Traumatic brain injury CT scans
- Expert-annotated hemorrhage masks
- 3D NIfTI format (.nii)

⚠️ Must comply with PhysioNet usage and licensing

---

##  Data Pipeline (v1)

### 1. 3D → 2D Conversion
- Extract slice-wise CT images and masks
- Maintain spatial correspondence

---

### 2. Data Format
- Format: `.npy`
- PNG removed

**Reason:**
- Preserve full **Hounsfield Unit (HU)** range  
- Enable accurate radiological processing

---

### 3. Ground Truth (Segmentation)

- Masks are used **directly as ground truth**
- Binary values: `[0, 255]`
- No explicit classification labels are generated

 Note:
- Hemorrhage presence can be derived from segmentation:
  - `hemorrhage = any(predicted_mask > 0)`

---

### 4. Preprocessing Pipeline

✔ Correct order (critical):

1. **Filtering (HU-based)**
2. **Cropping (brain region)**
3. **Windowing (multi-window strategy)**
4. **Normalization**

 Windowing strategy:
- Not limited to a single window
- Can include multiple channels:
  - Brain window
  - Blood window
  - Bone window

🔴 Important:
- Filtering must be applied **before windowing**
- HU values must be preserved until this stage

---

### 5. Dataset Split

- Strategy: **3D volume-level split**
- Prevents **data leakage across slices**

| Split | Samples |
|------|--------|
| Train | 2281 |
| Val   | 241  |
| Test  | 292  |

---

### 6. Data Structure

processed_data/
train/
images/
labels.csv
val/
images/
labels.csv
test/
images/
labels.csv


---

### 7. Validation Checks

- Mask values verified: `[0, 255]`
- Image-mask alignment confirmed
- File consistency validated
- Pipeline rebuilt cleanly

---

##  Input / Output

**Input:**
- 2D CT slices (`.npy`)

**Output:**
- Classification label (0 / 1)
- Segmentation mask (binary)

---

##  Evaluation Metrics

### Classification
- Accuracy  
- Precision  
- Recall  
- F1-score  

### Segmentation
- Dice Coefficient  
- Intersection over Union (IoU)  

---

##  Current Status

###  Completed
- Dataset acquisition  
- 3D → 2D conversion  
- Label generation  
- Preprocessing pipeline  
- Dataset splitting  
- Data validation  

---

###  Next Steps

- Train segmentation model (U-Net)
- Train classification model
- Model evaluation
- 3D modeling extension
- Feature extraction
- LLM + RAG integration
- Deployment (API + UI)

---

##  Future Directions

### Computer Vision
- 3-channel windowing (multi-window inputs)
- Brain region detection (auto-cropping)
- 3D volumetric models

### Multimodal AI
- CV + LLM integration
- Clinical reasoning layer

### Deployment
- FastAPI / Flask
- Dockerized inference
- Streamlit interface

---

##  System Modules

- **CV Module** → segmentation + detection  
- **ML Module** → classification  
- **LLM + RAG Module** → explanation layer  
- **UI Module** → user interaction  

---

## ⚠️ Disclaimer

This project is a **research prototype** and is **not intended for clinical use**.

---

##  Contact

**Seyed Ali Rashidi (Farid)**  
📧 farid.rash@gmail.com  

---

⭐ If you find this project useful, consider starring the repository
