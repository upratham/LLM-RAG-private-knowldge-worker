<!-- Generated: 2026-02-15T03:01:42.668030Z | Model: gpt-4.1-nano -->

# ML-flow-exp

## Overview
This repository is focused on machine learning experiment tracking and model management using MLflow, DagsHub, and Python. It contains scripts for training Random Forest classifiers on the Wine dataset, with capabilities for hyperparameter tuning, experiment logging, and artifact management. The code is suitable for data scientists and ML engineers aiming to automate and track their ML workflows.

## Key Features
- Training Random Forest classifiers on the Wine dataset.
- Experiment tracking with MLflow, including metrics, parameters, and artifacts.
- Integration with DagsHub for experiment management.
- Hyperparameter tuning using GridSearchCV.
- Automated logging with MLflow autologging.
- Visualization of confusion matrices.
- Model serialization and storage with MLflow.
- Support for multiple experiment runs and nested experiments.

## Architecture / How it Works
The repository comprises several Python scripts that perform data loading, model training, experiment tracking, and hyperparameter tuning:

- **Data Loading:** Uses `load_wine` from `sklearn.datasets`.
- **Model Training:** Implements Random Forest classifiers with specified hyperparameters.
- **Experiment Tracking:** Uses MLflow to log metrics, parameters, artifacts, and models.
- **Hyperparameter Tuning:** Employs `GridSearchCV` for hyperparameter optimization.
- **Artifact Management:** Saves confusion matrices and model files as artifacts.
- **Integration:** Uses DagsHub for experiment management and tracking.

The scripts configure MLflow experiments, start runs, and log relevant data for reproducibility and analysis.

## Notable Folders/Files
- **mlartifacts/**: Stores model artifacts, including trained models, configuration files (`conda.yaml`, `requirements.txt`), and logs.
- **mlruns/**: Contains MLflow experiment tracking data, including metrics, parameters, artifacts, and model versions.
- **src/**: Source code directory containing scripts:
  - `autolog.py`: Demonstrates MLflow autologging.
  - `file1.py`, `file2.py`: Scripts for training and logging models.
  - `hypertune1.py`: Performs hyperparameter tuning with GridSearchCV.
- **LICENSE**: MIT License for the repository.
- **.gitignore**: Specifies files to ignore in version control.

## Setup & Run
While explicit setup instructions are not provided, based on the code and artifacts:

1. **Install dependencies:**
   ```bash
   pip install mlflow scikit-learn pandas matplotlib seaborn dagshub
   ```
   Ensure that the required packages are installed, matching the versions in `requirements.txt` files within artifacts.

2. **Configure MLflow Tracking URI:**
   - For local experiments, use:
     ```python
     mlflow.set_tracking_uri("http://127.0.0.1:5000/")
     ```
   - For DagsHub, use:
     ```python
     mlflow.set_tracking_uri("https://dagshub.com/upratham2002/ML-flow-exp.mlflow")
     ```

3. **Run scripts:**
   - To train a model and log an experiment:
     ```bash
     python src/file1.py
     ```
   - To perform hyperparameter tuning:
     ```bash
     python src/hypertune1.py
     ```
   - To use autologging:
     ```bash
     python src/autolog.py
     ```

## How to Use
- **Training and Logging:**
  Run `file1.py` or `file2.py` to train a Random Forest on the Wine dataset, which will automatically log metrics, parameters, artifacts, and models to MLflow.

- **Experiment Management:**
  Use `mlflow.set_experiment()` to specify experiment names. Results are stored in the `mlruns` directory and can be visualized via MLflow UI:
  ```bash
  mlflow ui
  ```
  Then navigate to `http://localhost:5000` to view experiments.

- **Hyperparameter Tuning:**
  Use `hypertune1.py` to perform grid search over hyperparameters, with results logged as nested runs under a parent experiment.

- **Autologging:**
  Run `autolog.py` to enable automatic logging of models and metrics without manual log statements.

## Testing / CI
No explicit testing or CI/CD configurations are present in the repository. The focus appears to be on experiment tracking and model training.

## Deployment
No deployment scripts or instructions are included. The models are saved as artifacts within MLflow, ready for deployment or further evaluation.

## Contribution Notes
No specific contribution guidelines are provided. Users can contribute by creating new scripts, improving existing ones, or enhancing experiment tracking.

## Limitations / TODOs (Inferred)
- **Limited Dataset:** Only the Wine dataset is used; support for other datasets or data sources is not shown.
- **No explicit environment setup:** Users need to manually install dependencies.
- **Experiment reproducibility:** While artifacts are stored, detailed instructions for reproducing experiments are not provided.
- **Scalability:** Scripts are designed for small datasets and local runs; scaling to larger datasets or distributed environments is not addressed.
- **Documentation:** Additional documentation on setup, usage, and contribution would improve usability.

---

**Note:** If you require detailed setup instructions, environment configuration, or deployment strategies, please clarify or provide additional information.
