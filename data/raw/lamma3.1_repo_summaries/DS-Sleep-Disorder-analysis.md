<!-- Generated: 2026-02-15T01:16:34.750487Z | Model: llama3.1 -->

**DS-Sleep-Disorder-analysis**
==========================

Overview
--------

This repository contains a Jupyter Notebook-based project that aims to predict sleep disorder risk using lifestyle and basic health indicators. The project utilizes scikit-learn and TensorFlow for data cleaning, EDA, feature engineering, class imbalance handling, and model comparison.

**Key Features**

* Predicts sleep disorder risk from lifestyle and basic health indicators
* Utilizes scikit-learn and TensorFlow for data analysis and modeling
* Includes exploratory data analysis (EDA) and outlier checks
* Handles missing values and type inconsistencies in the target column
* Compares multiple machine learning models, including AdaBoost, Random Forest, and Neural Network

**Architecture / How it works**

The project follows a typical ML pipeline:

1. **Data collection & loading**
2. **Cleaning & preprocessing**
	* Handling missing values (notably in target column)
	* Encoding categorical features (OneHot/Ordinal)
	* Scaling numeric features (MinMaxScaler)
3. **Exploratory Data Analysis (EDA)**
	* Relationship exploration between lifestyle indicators and sleep disorder
	* Outlier checks (e.g., Z-score)
4. **Modeling**
	* Baseline model(s)
	* **AdaBoost**
	* **Random Forest**
	* Neural Network (ANN) using Keras/TensorFlow
5. **Class imbalance handling**
	* SMOTE oversampling used for training data

**Notable folders/files**

* `Sleep_Disorder_analysis.ipynb`: main notebook with the full pipeline
* `data/`: contains the Sleep Health & Lifestyle dataset (including an extended version)
* `requirements.txt`: lists dependencies required to run the project

**Setup & Run**

1. Clone this repository using `git clone https://github.com/upratham/DS-Sleep-Disorder-analysis.git`
2. Install dependencies by running `pip install -r requirements.txt` in your terminal
3. Open `Sleep_Disorder_analysis.ipynb` in a Jupyter Notebook environment and run the cells

**How to use**

1. Run the notebook using the instructions above
2. Explore the results, including accuracy, classification report, confusion matrix, and model comparison chart
3. Modify the code to experiment with different models or hyperparameters

**Testing / CI**

No testing framework is present in this repository.

**Deployment**

This project is designed for local execution on a Jupyter Notebook environment.

**Contribution notes**

Contributions are welcome! Please submit pull requests with clear explanations of changes made.

**Limitations / TODOs (inferred)**

* The project assumes access to the Sleep Health & Lifestyle dataset, which may not be publicly available
* The notebook does not include any error handling or logging mechanisms
* The model comparison chart is based on a single run and may not reflect optimal hyperparameters
