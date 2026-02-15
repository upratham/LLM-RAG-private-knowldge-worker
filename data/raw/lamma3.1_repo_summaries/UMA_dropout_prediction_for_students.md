<!-- Generated: 2026-02-15T01:26:01.396565Z | Model: llama3.1 -->

**UMA Dropout Prediction for Students**
=====================================

**Overview**
------------

This repository contains a machine learning model designed to predict the likelihood of students dropping out based on their profile. The model is built using Jupyter Notebooks and utilizes various libraries such as scikit-learn, pandas, and joblib.

**Key Features**

* Predicts student dropout probability based on 19 input features
* Utilizes ensemble methods (Random Forest Classifier and Logistic Regression) for base models
* Uses a meta-model to combine predictions from base models
* Supports both Gradio interface and Flask API for prediction

**Architecture/How it Works**
-----------------------------

1. The model is trained using a dataset containing student profiles.
2. The input features are fed into the base models (Random Forest Classifier and Logistic Regression) to generate predictions.
3. The meta-model combines the predictions from the base models to produce a final prediction.
4. The Gradio interface allows users to input their profile data and receive a prediction result.
5. The Flask API enables users to send JSON-formatted input data for prediction.

**Usage**
-----

### Gradio Interface

1. Run `app.py` using Jupyter Notebook or Python script.
2. Open the Gradio interface in your web browser at `http://localhost:7860`.
3. Input your profile data and receive a prediction result.

### Flask API

1. Run `flask_app.py` using Python script.
2. Send a POST request to `http://127.0.0.1:5000/predict` with JSON-formatted input data.
3. Receive the prediction result in JSON format.

**Code Structure**
-----------------

The repository contains the following files:

* `app.py`: Gradio interface code
* `flask_app.py`: Flask API code
* `load_data.ipynb`: Data loading and preprocessing script (not included in this excerpt)
* `model_five.joblib`, `model_four.joblib`, ..., `meta_model.joblib`: Trained model files

**Notes**
-----

* The code excerpts provided are for illustration purposes only. You should replace the placeholder values with your actual model loading, prediction logic, and data.
* This repository assumes you have Jupyter Notebook, Python 3.x, and required libraries installed on your system.

I hope this helps! Let me know if you have any questions or need further clarification.
