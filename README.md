# 🧠 CT Intracranial Hemorrhage Segmentation

Deep learning pipeline for **intracranial hemorrhage (ICH) detection and segmentation** from brain CT scans using volumetric (NIfTI) data and slice-wise modeling.

---

## 📌 Overview

This project focuses on building an end-to-end pipeline for analyzing traumatic brain injury (TBI) CT scans:

- Convert **3D CT volumes (NIfTI)** into 2D slices
- Train **segmentation models (U-Net)** to localize hemorrhage regions
- Extend to **classification and subtype detection**
- Explore **slice aggregation and 3D reasoning**

The goal is to move beyond simple classification and build a system that can **detect, localize, and analyze hemorrhage patterns**.

---

## 📂 Dataset

**Computed Tomography Images for Intracranial Hemorrhage Detection and Segmentation (v1.3.1)**

Source: https://physionet.org/content/ct-ich/1.3.1/  
Provider: PhysioNet

This dataset contains annotated brain CT scans for intracranial hemorrhage (ICH) detection and segmentation, with pixel-wise labels provided by expert radiologists.

### Includes:

- ✅ CT volumes in **NIfTI format**
- ✅ Pixel-wise **segmentation masks**
- ✅ Slice-level labels
- ✅ Hemorrhage subtypes:
  - Intraventricular (IVH)
  - Intraparenchymal (IPH)
  - Subarachnoid (SAH)
  - Epidural (EDH)
  - Subdural (SDH)

---

## ⚙️ Pipeline

### 1. Preprocessing
- Load NIfTI volumes
- Apply CT windowing (brain window)
- Extract 2D slices
- Align slices with segmentation masks

### 2. Segmentation
- Model: U-Net (baseline)
- Input: 2D CT slice
- Output: hemorrhage mask

### 3. Classification (optional)
- Binary: hemorrhage vs normal
- Multi-label: hemorrhage subtypes

### 4. Advanced (future work)
- Slice aggregation (sequence modeling)
- 3D modeling (3D CNN / hybrid approaches)
- Attention-based models

---

## 🧠 Why This Project

Most basic approaches only classify CT slices.

This project focuses on:

- **Localization (segmentation)** instead of only classification
- Leveraging **radiologist annotations**
- Bridging **2D and 3D medical imaging workflows**

---

## 📊 Challenges

- Small dataset size → risk of overfitting
- Limited acquisition diversity
- Class imbalance across hemorrhage types

---

## 🚀 Future Improvements

- Data augmentation strategies for medical imaging
- Transfer learning from large-scale medical datasets
- Integration with external datasets (e.g. RSNA)
- Real-time inference pipeline
- Clinical-style visualization tools

---

## 🛠️ Tech Stack

- Python
- PyTorch / TensorFlow
- NumPy / OpenCV
- NiBabel (NIfTI processing)
- Matplotlib

---

## 📁 Project Structure
ct-ich-segmentation/
│
├── data/
├── notebooks/
├── src/
│ ├── preprocessing/
│ ├── models/
│ ├── training/
│ └── utils/
│
├── outputs/
├── requirements.txt
└── README.md

---

## 📌 Status

🚧 Work in progress — building preprocessing and baseline segmentation model.

---

## 🤝 Contributions

Open to collaboration in:

- Medical imaging
- Computer vision
- Deep learning for healthcare

---

## ⚠️ Disclaimer

This project is for **research and educational purposes only** and is not intended for clinical use.
