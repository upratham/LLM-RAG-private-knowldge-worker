<!-- Generated: 2026-02-15T03:03:55.145268Z | Model: gpt-4.1-nano -->

# Face-Differentiator

## Overview
Face-Differentiator is a Python-based project that utilizes the FaceNet model to perform face recognition and comparison. It is designed for developers and researchers interested in face verification tasks, allowing them to determine whether two images contain the same person or different individuals based on facial embeddings.

## Key Features
- Uses the Keras implementation of FaceNet for face embedding extraction.
- Compares facial embeddings to determine similarity.
- Simple command-line interface for inputting images and directories.
- Threshold-based decision making for face verification.
- Pretrained on ImageNet and MS-Celeb-1M datasets, with weights ported from David Sandberg's TensorFlow FaceNet repository.

## Architecture / How it Works
The core functionality is implemented in the `face.py` script, which performs the following steps:
1. Loads the FaceNet model via the `keras_facenet` library.
2. Prompts the user for:
   - The path to a reference image.
   - The directory containing images to compare against.
3. For each image in the specified directory:
   - Extracts facial embeddings using FaceNet.
   - Calculates the squared Euclidean distance between the reference image's embedding and the current image's embedding.
   - Compares the distance to a predefined threshold to decide if the images are of the same person or different.

The `README.md` provides an overview of the approach, emphasizing embedding extraction, distance calculation, and threshold-based classification.

## Notable Folders/Files
- `face.py`: Main script that performs face comparison operations.
- `README.md`: Documentation and usage instructions.
- `abhi.jpg`, `adityaraj.jpg`, `adityaraj2.jpg`: Sample images, likely used for testing or demonstration purposes.
- `keras_facenet`: (implied dependency) Python library used for FaceNet embedding extraction.

## Setup & Run
### Prerequisites
- Python environment with `keras_facenet` installed.
- Access to the internet for installing dependencies:
  ```bash
  pip install keras-facenet
  ```

### Running the Script
1. Ensure all dependencies are installed.
2. Execute the script:
   ```bash
   python face.py
   ```
3. When prompted:
   - Enter the path to the reference image.
   - Enter the path to the directory containing images to compare.

### Example
```
ENTER PATH OF 1st IMG: /path/to/reference.jpg
ENTER PATH to the IMG DIRECTORY: /path/to/images/
```

The script will process each image in the directory, outputting whether each is the same or different compared to the reference image based on the calculated distance.

## How to Use
- Provide a reference image and a directory of images.
- The script will compare each image in the directory to the reference.
- Results will be printed as "SAME" or "DIFFERENT" based on the threshold.

### Example Output
```
[0.1234]
SAME

[1.5678]
DIFFERENT
```

*Note:* The threshold value (`tresh=1.5`) can be adjusted in the `get_distance` function to tune sensitivity.

## Testing / CI
- No explicit testing or CI configurations are present in the repository.
- Testing appears to be manual via the command-line interface.

## Deployment
- No deployment scripts or instructions are provided.
- The project is intended for local use or integration into larger systems with modifications.

## Contribution Notes
- No specific contribution guidelines are included.
- Users can fork the repository, modify `face.py`, or enhance the functionality as needed.

## Limitations / TODOs (Inferred)
- The script processes images sequentially and relies on user input, which may not be suitable for automation.
- The threshold value is fixed; adaptive or dynamic thresholding could improve accuracy.
- Error handling (e.g., missing files, no face detected) is not explicitly implemented.
- The dataset and model weights are preloaded; updates or retraining are not covered.
- The repository lacks comprehensive documentation, tests, or deployment instructions.

---

**Note:** If you require further details or clarification, such as the structure of the face embeddings or integration options, please specify.
