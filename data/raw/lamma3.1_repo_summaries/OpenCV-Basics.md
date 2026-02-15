<!-- Generated: 2026-02-15T01:31:20.005976Z | Model: llama3.1 -->

**OpenCV-Basics**
================

### Overview

This repository provides a basic introduction to OpenCV, a popular computer vision library. It is intended for individuals who want to learn the fundamentals of image and video processing using Python.

### Key Features

* Demonstrates how to capture video from a URL
* Displays a camera preview window with adjustable size
* Includes example images and logos for manipulation
* Utilizes OpenCV 2.x (cv2) library

### Architecture / How it works

The repository consists of a single Python script, `camera.py`, which uses the cv2 library to capture video from a specified URL. The script also includes error handling and window management using OpenCV functions.

### Notable folders/files

* `opencv_bootcamp_assets_NB4.zip`: A zip archive containing additional assets for OpenCV bootcamp
* `Logo_Manipulation.png` and other image files: Example images used in the repository
* `camera.py`: The main Python script that demonstrates video capture using cv2

### Setup & Run

1. Clone the repository using `git clone https://github.com/upratham/OpenCV-Basics.git`
2. Install OpenCV library using `pip install opencv-python`
3. Run the `camera.py` script using `python camera.py`

Note: The script expects a device index as an argument, but it is not used in this example.

### How to use

1. Run the `camera.py` script to display a camera preview window
2. Use the `cv2.waitKey(1)` function to pause the video playback and adjust the window size using OpenCV functions

### Testing / CI

No testing or continuous integration scripts are present in this repository.

### Deployment

Not applicable, as this is a development repository.

### Contribution notes

Contributions are welcome! Please submit pull requests with clear explanations of changes made.

### Limitations / TODOs (inferred)

* The script does not handle errors when capturing video from the specified URL.
* The window size and position are not saved between runs.
* Additional features, such as image processing or object detection, could be added to enhance the repository.
