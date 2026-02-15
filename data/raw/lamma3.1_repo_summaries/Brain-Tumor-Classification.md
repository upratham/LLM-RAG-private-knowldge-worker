<!-- Generated: 2026-02-15T01:24:47.104577Z | Model: llama3.1 -->

**Brain Tumor Classification for MRI Datasets using Deep Learning**
===========================================================

**Overview**
------------

This repository contains a deep learning model designed to classify brain tumors from MRI images. The project was conducted as part of a research internship at the Vishwakarma University Research Center of Excellence and achieved a 95% testing accuracy.

**Key Features**
---------------

*   Classifies brain tumors using MRI datasets with a deep learning approach
*   Utilizes the Kaggle dataset for training and testing
*   Achieved 95% testing accuracy
*   Uses data augmentation to enhance the dataset
*   Implemented using TensorFlow, Keras, and OpenCV

**Architecture / How it works**
-----------------------------

The project uses a deep learning model implemented in Jupyter Notebook. The architecture is based on Convolutional Neural Networks (CNNs) with transfer learning from pre-trained models.

### Notable Folders/Files

*   `classifier`: Contains the implementation of the deep learning model
*   `requirements.txt`: Lists the necessary dependencies for running the project
*   `Final_Brain_Tumor_Classification.ipynb`: The main Jupyter Notebook file containing the code and results

**Setup & Run**
----------------

1.  Clone the repository using `git clone https://github.com/upratham/Brain-Tumor-Classification.git`
2.  Navigate to the project directory using `cd brain-tumor-classification`
3.  Install the necessary dependencies using `pip install -r requirements.txt`

**How to use**
--------------

1.  Run the Jupyter Notebook file `Final_Brain_Tumor_Classification.ipynb` to view the results and code
2.  Use the `classifier` folder to implement the deep learning model for your own dataset

**Testing / CI**
-----------------

No testing or continuous integration scripts are present in this repository.

**Deployment**
--------------

No deployment instructions are provided.

**Contribution notes**
----------------------

Contributions from the community are welcome. To contribute:

1.  Fork the repository
2.  Create a new branch (`git checkout -b feature-branch`)
3.  Make your changes and commit them (`git commit -m 'Add new feature'`)
4.  Push to the branch (`git push origin feature-branch`)
5.  Create a new Pull Request

**Limitations / TODOs**
-----------------------

*   The project does not include any error handling or debugging mechanisms
*   The dataset used for training and testing is not included in this repository
*   The research paper cited in the README.md file may not be publicly available due to copyright restrictions.
