<!-- Generated: 2026-02-15T03:02:08.294603Z | Model: gpt-4.1-nano -->

# Non-linear-dimensionality-reduction

Repository for exploring spectral clustering and nonlinear dimensionality reduction techniques on the Iris dataset.

---

## Overview

This repository provides implementations and analyses of spectral clustering and nonlinear dimensionality reduction methods applied to the Iris dataset. It is intended for students, researchers, and practitioners interested in clustering algorithms and manifold learning techniques. The main focus is on understanding how spectral clustering compares to traditional methods like K-Means and how various nonlinear embedding methods reveal the structure of the data.

---

## Key Features

- **Spectral Clustering from Scratch:** Implements spectral clustering algorithm manually, including affinity matrix construction, eigen-decomposition, and clustering.
- **Comparison with K-Means:** Evaluates the effectiveness of spectral clustering versus standard K-Means on the Iris dataset.
- **Nonlinear Dimensionality Reduction Techniques:**
  - Multidimensional Scaling (MDS)
  - Isomap
  - Locally Linear Embedding (LLE)
- **Visualization:** Generates 2D plots of embeddings colored by species to analyze class separation.
- **Parameter Analysis:** Investigates the impact of neighborhood size parameters in Isomap and LLE.

---

## Architecture / How it Works

The core logic resides within a Jupyter Notebook (`HW8.ipynb`), which sequentially performs:

1. Data loading and preprocessing.
2. Construction of affinity matrices for spectral clustering.
3. Eigen-decomposition and clustering.
4. Application of nonlinear embedding algorithms.
5. Visualization and analysis of results.

The notebook leverages scikit-learn's implementations for MDS, Isomap, and LLE, while the spectral clustering is implemented manually.

---

## Notable Folders/Files

- `HW8.ipynb`  
  The main Jupyter Notebook containing all code, visualizations, and analysis. It is the primary interface for running experiments and viewing results.

- `Data_Iris.csv`  
  The dataset in CSV format. Contains the features and labels of the Iris dataset, used for clustering and visualization.

- `.gitignore`  
  Specifies files and folders to ignore in version control.

- `LICENSE`  
  Contains the MIT license under which this project is released.

- `README.md`  
  This documentation file.

---

## Setup & Run

### Requirements

Ensure you have Python 3.x installed along with the necessary libraries:

- numpy
- pandas
- matplotlib
- scikit-learn
- jupyter

### Installation

Install dependencies via pip:

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

### Running the Notebook

1. Clone the repository:

```bash
git clone https://github.com/upratham/Non-linear-dimensionality-reduction.git
cd Non-linear-dimensionality-reduction
```

2. Launch Jupyter Notebook:

```bash
jupyter notebook HW8.ipynb
```

3. Open `HW8.ipynb` in your browser and run the cells sequentially.

**Note:** Make sure `Data_Iris.csv` is in the same directory as the notebook or update the path in the code accordingly.

---

## How to Use

- **Execute the notebook cells** to perform spectral clustering, apply nonlinear embeddings, and generate plots.
- **Modify parameters** such as neighborhood sizes (`k`) in Isomap and LLE to observe their effects.
- **Analyze visualizations** to understand class separation and the effectiveness of each method.

---

## Testing / CI

No explicit testing or continuous integration setup is mentioned or present in the repository.

---

## Deployment

This project is designed for educational and exploratory purposes within a Jupyter Notebook environment. There is no deployment process involved.

---

## Contribution Notes

No contribution guidelines are provided in the repository. Feel free to fork and modify the notebook for your own experiments.

---

## Limitations / TODOs (Inferred)

- The spectral clustering implementation is basic and may not include optimizations for large datasets.
- The analysis is limited to the Iris dataset; applicability to larger or more complex datasets is not demonstrated.
- Parameter tuning (e.g., affinity kernel parameters, number of neighbors) could be expanded.
- Additional nonlinear methods or clustering algorithms could be integrated for comparison.
- Automated testing or validation routines are not present.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**For more details, see the main notebook:** [HW8.ipynb](https://github.com/upratham/Non-linear-dimensionality-reduction/blob/main/HW8.ipynb)
