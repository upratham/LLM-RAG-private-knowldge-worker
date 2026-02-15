<!-- Generated: 2026-02-15T02:58:50.943948Z | Model: gpt-4.1-nano -->

# Breast-Cancer-Segmentation

## Overview
This repository focuses on deep-learning-based binary segmentation of ultrasound images for breast cancer detection. It provides tools and workflows to preprocess data, train segmentation models (U-Net, DeepLabV3+, MultiResUNet), and evaluate their performance. The target audience includes researchers, medical imaging specialists, and machine learning practitioners working on medical image segmentation, particularly in breast cancer diagnosis.

## Key Features
- Implements multiple segmentation architectures: U-Net, DeepLabV3+, MultiResUNet.
- End-to-end workflow: data preprocessing, model training, and evaluation.
- Utilizes Jupyter Notebooks for an interactive and flexible development process.
- Supports evaluation metrics such as Dice coefficient and IoU.
- Organized data structure with separate folders for training, testing, and validation images and masks.
- License: MIT License.

## Architecture / How it Works
The project is structured around three main notebooks:
- `data_preprocessing.ipynb`: Handles image resizing, normalization, mask alignment, and dataset splitting.
- `train.ipynb`: Builds and trains the selected segmentation model, tracking performance metrics and saving checkpoints.
- `eval.ipynb`: Performs inference on test data, visualizes predictions, and computes evaluation metrics.

Supporting source files in the `src/` directory include:
- Model definitions (`model_unet.py`, `model2_DeeplabV3.py`, `model3_MultiResUNET.py`)
- Metrics calculations (`metrics.py`)
- Additional utility scripts (not explicitly listed but implied)

The notebooks and source files work together to facilitate a modular segmentation pipeline.

## Notable Folders/Files
- `data/`: Contains subfolders for training (`train`), testing (`test`), and validation (`valid`) images and masks.
- `src/`: Source code for model architectures and metrics, crucial for customization or extension.
- `requirements.txt`: Lists dependencies needed to run the notebooks.
- `.gitignore`, `LICENSE`, `README.md`: Standard project files for version control, licensing, and documentation.

## Setup & Run
### 1) Environment Setup
Create and activate a virtual environment:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 2) Install Dependencies
```bash
pip install -r requirements.txt
```
*(Ensure you have compatible versions of TensorFlow or PyTorch installed as per your preference; the notebooks are designed to work with either backend.)*

## How to Use
### Data Preprocessing
Open and run:
```bash
jupyter notebook data_preprocessing.ipynb
```
This step prepares images and masks, performs normalization, resizing, and dataset splitting.

### Model Training
Open and run:
```bash
jupyter notebook train.ipynb
```
This notebook loads preprocessed data, constructs the selected model architecture, trains it, and saves the best model checkpoints.

### Model Evaluation / Inference
Open and run:
```bash
jupyter notebook eval.ipynb
```
This step generates predictions on test data, visualizes results (input image, ground truth, predicted mask), and computes metrics like Dice and IoU.

## Testing / CI
No explicit testing or CI configurations are mentioned in the provided data. If present, they are not detailed here.

## Deployment
Deployment procedures are not specified. The focus appears to be on model development and evaluation within notebooks.

## Contribution Notes
No contribution guidelines are provided in the current documentation.

## Limitations / TODOs (Inferred)
- The repository relies heavily on Jupyter Notebooks; integrating scripts for automation could improve usability.
- Support for different deep learning backends (TensorFlow vs PyTorch) may require adaptation.
- No explicit mention of data augmentation strategies or hyperparameter tuning workflows.
- Potential need for more detailed instructions on environment setup, especially GPU support.
- Future enhancements could include a command-line interface or API for inference.

---

*Note:* If you require further details on specific scripts or configurations, please clarify or provide additional information.
