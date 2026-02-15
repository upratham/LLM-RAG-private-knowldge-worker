<!-- Generated: 2026-02-15T01:22:04.822847Z | Model: llama3.1 -->

**MLOps-Insurance-Project**
==========================

Overview
--------

This is an end-to-end MLOps project for an insurance ML use case, including a pipeline and app with Dockerized deployment.

Key Features
-------------

* Pipeline: A modular and scalable pipeline for training and deploying machine learning models.
* App: A web application for interacting with the trained models.
* Dockerization: The entire project is containerized using Docker for easy deployment and reproducibility.
* Logging: Custom logging configuration for efficient debugging and monitoring.

Architecture / How it Works
---------------------------

The project consists of several components:

1. **Pipeline**: Located in `src/pipline`, this module contains the training and prediction pipelines.
2. **App**: Located in `app.py`, this script sets up the web application using FastAPI.
3. **Dockerization**: The entire project is containerized using Docker, with a `Dockerfile` located at the root of the repository.

Notable Folders/Files
----------------------

* `src/pipline`: Contains the training and prediction pipelines.
* `app.py`: Sets up the web application using FastAPI.
* `config/model.yaml` and `config/schema.yaml`: Configuration files for model and schema definitions.
* `src/logger/__init__.py`: Custom logging configuration.

Setup & Run
------------

1. Clone the repository: `git clone https://github.com/upratham/MLOps-Insurance-Project.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Build Docker image: `docker build -t mlops-insurance-project .`
4. Run Docker container: `docker run -p 8000:8000 mlops-insurance-project`

How to Use
------------

1. Interact with the web application by visiting `http://localhost:8000` in your browser.
2. Use the API endpoints to interact with the trained models.

Testing / CI
-------------

No testing framework is explicitly mentioned, but the project uses Dockerization for reproducibility and ease of deployment.

Deployment
-----------

The project uses Dockerization for easy deployment. To deploy, simply build and run the Docker image as described above.

Contribution Notes
------------------

Contributions are welcome! Please follow standard professional guidelines when contributing to this repository.

Limitations / TODOs
-------------------

* **Inference**: The project does not explicitly mention any limitations or TODOs.
* **Testing framework**: No testing framework is explicitly mentioned, which may make it difficult to ensure the quality of the codebase.
