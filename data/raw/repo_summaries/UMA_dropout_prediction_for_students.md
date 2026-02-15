<!-- Generated: 2026-02-15T03:00:56.003390Z | Model: gpt-4.1-nano -->

# UMA_dropout_prediction_for_students

## Overview
This repository provides a machine learning-based system to predict whether a student is likely to drop out. It is designed for educational institutions, data scientists, and developers interested in student retention analytics. The system leverages multiple models and offers both a Jupyter Notebook interface and a Flask API for deployment and integration.

## Key Features
- **Multi-model ensemble prediction:** Combines predictions from several pre-trained models for improved accuracy.
- **Interactive web interface:** Uses Gradio to provide a user-friendly prediction interface.
- **API endpoint:** Flask app exposes a REST API for programmatic access to predictions.
- **Data preprocessing and feature engineering:** Includes notebooks for outlier detection, feature engineering, and data cleaning.
- **Model persistence:** Pre-trained models are stored as `.joblib` files for quick loading and inference.
- **Support for real-time predictions:** Both the web interface and API facilitate real-time student dropout risk assessment.

## Architecture / How it Works
The system primarily consists of:
- **Pre-trained models:** Stored as `.joblib` files, including multiple classifiers and a meta-model.
- **Prediction pipeline:** Inputs are processed into feature vectors, predictions are made by base models, then combined via a meta-model.
- **Web interface:** Built with Gradio, allowing users to input student data and receive dropout risk predictions.
- **API service:** Flask application (`flask_app.py`) exposes an endpoint for external systems to request predictions.

## Notable Folders/Files
- **`app.py`**: Contains the Gradio interface code for interactive predictions.
- **`flask_app.py`**: Flask server exposing a REST API for predictions.
- **`load data.ipynb`**, **`Phaseone.ipynb`**, **`Outliers Detection Removal amd Feature Engineering.ipynb`**, **`still_data_arranging.ipynb`**: Jupyter notebooks for data cleaning, feature engineering, and exploratory analysis.
- **`model_*.joblib`**: Serialized pre-trained models used for inference.
- **`base_proyecto.xlsx`**: Likely contains raw or processed data used during model training or analysis.
- **`meta_model.joblib`**: Meta-model that combines base model predictions into final output.
- **`Assetto_Corsa_Competizione_--_fitgirl-repacks.site_--_/MD5/`**: Unrelated files, possibly included as artifacts or accidental uploads.

## Setup & Run
### Prerequisites
- Python environment with necessary libraries (`scikit-learn`, `pandas`, `numpy`, `gradio`, `flask`, `joblib`)
- Pre-trained model files (`model_one.joblib`, etc.) in the repository

### Running the Web Interface
1. Install dependencies:
```bash
pip install gradio pandas numpy scikit-learn joblib
```
2. Launch the Gradio app:
```bash
python app.py
```
This will start a local server and open a web interface for predictions.

### Running the Flask API
1. Install dependencies:
```bash
pip install flask pandas numpy scikit-learn joblib
```
2. Run the Flask server:
```bash
python flask_app.py
```
The API will be available at `http://127.0.0.1:5000/predict`.

## How to Use
### Web Interface
- Access the URL provided after running `app.py`.
- Fill in student features such as attendance, grades, credits, etc.
- Submit to receive a prediction whether the student is likely to drop out.

### API Usage
Send a POST request with JSON data to `http://127.0.0.1:5000/predict`. Example payload:
```json
{
  "REGISTERED_ATTENDANCES": 10,
  "ASISTENCIAS_TOMADAS ": 8,
  "ENROLLED_COURSES": 5,
  "APPROVED_COURSES": 4,
  "ENROLLED_CREDITS": 20,
  "APPROVED_CREDITS": 15,
  "PAYMENT_DELAYS_DAYS": 0,
  "NUMBER_OF_INSTALLMENTS": 1,
  "CREDITS": 60,
  "GRADE": 80,
  "SEMESTER": 6,
  "Year_Corrected": 2023,
  "AGE_ADJUSTED": 22,
  "HAS_FAILING_GRADES": 0,
  "FINAL_GPA": 3.5,
  "STATE_R": 0,
  "Attendance_Rate": 0.8,
  "Total_Semesters": 8,
  "Active_Enrollment_Ratio": 0.9
}
```
Response:
```json
{
  "prediction": 0.75,
  "status": "Likely to Stay"
}
```

## Testing / CI
No explicit testing or CI configurations are present in the repository. Notable notebooks may include data validation steps, but automated testing is not documented.

## Deployment
- The Flask app can be deployed on any server supporting Python.
- The Gradio interface can be hosted locally or shared publicly via the `share=True` parameter.
- For production, consider deploying the Flask app with a WSGI server like Gunicorn and setting up HTTPS.

## Contribution Notes
No contribution guidelines are provided. For improvements, fork the repository, implement changes, and submit a pull request.

## Limitations / TODOs (Inferred)
- **Model details unspecified:** The exact models and their training procedures are not documented.
- **Data privacy:** Handling of sensitive student data is not discussed.
- **Model explainability:** No explanation methods are integrated.
- **Unclear data source:** The origin of datasets and feature engineering steps are not fully detailed.
- **Uncertain deployment instructions:** No Docker or containerization guidance is provided.
- **Potential for further automation:** CI/CD pipelines, automated testing, and model retraining workflows are not present.

---

*Note:* If you require detailed instructions on data preprocessing, model training, or deployment best practices, please provide additional information or specific files.
