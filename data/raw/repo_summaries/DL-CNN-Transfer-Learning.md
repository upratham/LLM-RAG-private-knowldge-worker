<!-- Generated: 2026-02-15T03:01:03.872666Z | Model: gpt-4.1-nano -->

# DL-CNN-Transfer-Learning

## Overview
This repository provides a deep learning solution for classifying images of flowers into 10 different categories. It is designed for developers, data scientists, and students interested in image classification using Convolutional Neural Networks (CNN) and transfer learning with VGG16. The implementation leverages TensorFlow and Keras, with code structured in Jupyter Notebooks and Python scripts.

## Key Features
- Implements a custom CNN architecture for multi-class flower classification.
- Utilizes transfer learning with the pre-trained VGG16 model to improve accuracy.
- Supports training, evaluation, and visualization of results.
- Handles image preprocessing, including resizing and label extraction.
- Designed with GPU compatibility and memory management in mind.

## Architecture / How It Works
The repository's architecture centers around Python scripts that handle data preprocessing, model building, training, and evaluation:

- **`src/data_preprocess.py`**: Loads images from the dataset, resizes them to 200×200 pixels, and encodes labels based on filename conventions.
- **`src/models.py`**: Defines two models:
  - A custom CNN with multiple convolutional, pooling, dropout, and dense layers.
  - A transfer learning model based on VGG16, with options to freeze or fine-tune the convolutional base.
- **`src/train.py`**: Manages data splitting, model compilation, and training routines.
- **`src/eval.ipynb`**: Jupyter Notebook for model evaluation, visualization, and performance analysis.

The dataset is organized in the `data/flowers` directory, with images categorized into subfolders or named to facilitate label extraction.

## Notable Folders/Files
- **`src/`**: Contains all source code files for data preprocessing, model definitions, training, and evaluation.
- **`data/flowers/`**: Dataset folder with flower images in `.jpg` format.
- **`requirements.txt`**: Lists dependencies required to run the project.
- **`README.md`**: This documentation file.

## Setup & Run
### 1. Environment Setup
Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare Data
Ensure your images are stored in `data/flowers/`. Filenames should start with the class name followed by a digit (e.g., `daisies1.jpg`) to match label extraction logic.

### 4. Train the Model
Run the training script:

```bash
python src/train.py
```

This will train the CNN model with default parameters (50 epochs, batch size 64).

## How to Use
### Training
The default training process uses the `train.py` script, which:
- Loads and preprocesses images.
- Splits data into training and testing sets (80/20).
- Builds the CNN model.
- Starts training with specified epochs and batch size.

### Evaluation
Open and execute the Jupyter Notebook:

```bash
jupyter notebook src/eval.ipynb
```

Use the notebook to:
- Load the trained model.
- Evaluate accuracy on test data.
- Generate confusion matrices and plots for performance analysis.

### Example
Suppose you want to train with different parameters or models:
- Modify `src/train.py` to select the model (custom CNN or VGG16).
- Adjust hyperparameters like epochs or batch size.
- Re-run the training script.

## Testing / CI
No explicit testing or Continuous Integration (CI) setup is mentioned in the provided data.

## Deployment
No deployment instructions are provided. The trained models can be saved and integrated into applications as needed.

## Contribution Notes
No specific contribution guidelines are included in the provided data.

## Limitations / TODOs (Inferred)
- The current setup assumes filenames start with class names; inconsistent naming may cause label errors.
- Transfer learning model's `transfer_flag` is set to `False` by default; fine-tuning is optional.
- Callbacks like EarlyStopping are defined but commented out; enabling them could improve training.
- No explicit validation set or hyperparameter tuning is described.
- The dataset appears to be static; adding data augmentation could enhance model robustness.
- Testing and deployment pipelines are not detailed; adding these could improve usability.

---

*For further details, refer to the code files and the Jupyter Notebook in the `src/` directory.*
