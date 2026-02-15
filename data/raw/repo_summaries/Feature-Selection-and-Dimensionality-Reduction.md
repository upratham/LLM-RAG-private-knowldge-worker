<!-- Generated: 2026-02-15T03:02:01.856816Z | Model: gpt-4.1-nano -->

# Feature-Selection-and-Dimensionality-Reduction

## Overview
This repository provides a comprehensive machine learning pipeline focused on feature selection and dimensionality reduction techniques applied to an air quality classification dataset. It is designed for data scientists and machine learning practitioners interested in evaluating different methods for reducing feature space and improving classification performance. The pipeline includes data preprocessing, feature engineering, model training, and evaluation, along with visualization of results.

## Key Features
- Loads and preprocesses pollution dataset with label encoding and handling of negative values.
- Implements multiple feature selection and dimensionality reduction methods:
  - Univariate feature selection (Chi-square)
  - Random Forest feature importance
  - Principal Component Analysis (PCA)
  - Linear Discriminant Analysis (LDA)
- Trains classifiers (SVM and Gaussian Naive Bayes) across multiple train/test splits.
- Evaluates and visualizes model accuracy versus number of features/components.
- Generates detailed plots for feature importance, PCA, LDA, and accuracy trends.
- Logs detailed insights and results for reproducibility and analysis.

## Architecture / How it Works
The repository is organized into modular Python scripts within the `src/` directory:
- `data_import.py`: Loads the dataset.
- `data_preprocessing.py`: Cleans data and encodes labels.
- `feature_engineering.py`: Performs feature selection and dimensionality reduction, and creates visualizations.
- `model_training.py`: Trains classifiers with different feature sets and records results.
- `model_eval.py`: Analyzes results, computes statistics, and generates evaluation plots.

The workflow typically involves:
1. Loading data.
2. Preprocessing data.
3. Applying feature engineering methods.
4. Training classifiers over multiple iterations and feature sets.
5. Evaluating and visualizing results.

## Notable Folders/Files
- `data/`: Contains the raw pollution dataset (`pollution_dataset.csv`).
- `src/`: Core scripts implementing data loading, preprocessing, feature engineering, training, and evaluation.
- `result/`: Stores generated plots, textual reports, and intermediate datasets.
- `logs/`: Contains log files for each processing step.
- `requirements.txt`: Lists dependencies needed to run the pipeline.

## Setup & Run
1. Clone the repository:
```bash
git clone https://github.com/upratham/Feature-Selection-and-Dimensionality-Reduction.git
cd Feature-Selection-and-Dimensionality-Reduction
```
2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the evaluation script:
```bash
cd src
python model_eval.py
```
This will execute the entire pipeline, including data loading, preprocessing, feature engineering, training, and evaluation, generating plots and reports in the `result/` directory.

## How to Use
- To perform only feature engineering visualizations:
```bash
python feature_engineering.py
```
- To retrain models with fresh results:
```bash
python model_training.py
```
- To evaluate and visualize results:
```bash
python model_eval.py
```
You can modify parameters such as the number of iterations (`iter`) or the K values for features/components inside the scripts as needed.

## Testing / CI
No explicit testing or CI configurations are mentioned. The scripts include logging for debugging and traceability.

## Deployment
There is no deployment process specified. The code is intended for local analysis and experimentation.

## Contribution Notes
No specific contribution guidelines are provided in the documentation. Feel free to fork, modify, and improve the scripts.

## Limitations / TODOs (Inferred)
- The dataset path is hardcoded; flexibility for custom datasets or paths is limited unless scripts are modified.
- The number of iterations and K values are fixed; parameterization could improve usability.
- No explicit unit tests or validation steps are included.
- Visualization styles and analysis depth could be expanded for more comprehensive insights.
- The pipeline assumes the dataset has specific columns (`Air Quality` and features); adaptation may be needed for different datasets.

---

*Note:* If you have specific questions about certain parts of the code or need further customization, please clarify.
