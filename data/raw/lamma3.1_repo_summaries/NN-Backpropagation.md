<!-- Generated: 2026-02-15T01:29:26.839160Z | Model: llama3.1 -->

**NN-Backpropagation Repository**
=====================================

### Overview

This repository contains a minimal implementation of a fully-connected neural network built from scratch using NumPy. It demonstrates how to define a neural network class, implement forward propagation and backpropagation manually, and train the network using gradient descent.

### Key Features

*   Fully-connected neural network implemented from scratch using NumPy
*   Forward propagation and backpropagation implemented manually
*   Training loop with gradient descent for optimization
*   Error plot to visualize training error over iterations

### Architecture / How it works

The repository consists of a single Jupyter notebook, `back_propogation.ipynb`, which contains the neural network implementation, training loop, and error plot. The notebook uses NumPy for numerical computations and matplotlib for plotting.

### Notable folders/files

*   **`back_propogation.ipynb`**: Main Jupyter notebook with the neural network implementation, training loop, and error plot
*   **`README.md`**: This file (you're reading it!)

### Setup & Run

To run the repository, follow these steps:

1.  Clone the repository using `git clone https://github.com/upratham/NN-Backpropagation.git`
2.  Install the required dependencies using `pip install numpy matplotlib jupyter`

You can then open the `back_propogation.ipynb` notebook in Jupyter to run the code.

### How to use

To use this repository, follow these steps:

1.  Open the `back_propogation.ipynb` notebook in Jupyter
2.  Run each cell in the notebook to execute the code
3.  Observe the training error plot and adjust hyperparameters as needed

### Testing / CI

No testing or continuous integration (CI) scripts are present in this repository.

### Deployment

This repository is not intended for deployment; it's a demonstration of neural network implementation from scratch using NumPy.

### Contribution notes

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes.

### Limitations / TODOs (inferred)

*   The repository does not include any error handling or debugging mechanisms.
*   The training loop uses gradient descent for optimization; more advanced optimizers may be beneficial for larger networks.
*   No regularization techniques are implemented to prevent overfitting.
