<!-- Generated: 2026-02-15T00:39:37.164936Z | Model: llama3.1 -->

**LLM-Meeting-Minutes-Generation**
=====================================

Overview
--------

This repository contains a simple Gradio web app that takes an uploaded audio file, generates a transcript, and then produces clean meeting minutes in Markdown (summary, discussion points, takeaways, and action items with owners).

Key Features
-------------

*   Upload audio files (mp3 / wav / m4a, etc.)
*   Automatic transcription using Google GenAI
*   Generates structured meeting minutes in Markdown

Architecture/How it Works
-------------------------

The app uses the following components:

1.  **Gradio**: A Python library for building web apps.
2.  **Google GenAI**: For automatic transcription of uploaded audio files.
3.  **Hugging Face Router**: For using pre-trained Llama models to generate meeting minutes.

Notable Folders/Files
----------------------

*   `app.py`: The main entrypoint of the Gradio app.
*   `notebooks/`: Original development notebooks (not used in this version).
*   `requirements.txt`: Dependencies required for running the app.

Setup & Run
------------

To run the app locally:

1.  Install dependencies using `pip install -r requirements.txt`.
2.  Set environment variables:
    *   `HF_TOKEN` (Hugging Face token, add as a Space Secret).
    *   `GOOGLE_API_KEY` (Google GenAI key, add as a Space Secret).
3.  Run the app using `python app.py`.

How to Use
------------

1.  Upload an audio file (mp3 / wav / m4a, etc.) using the Gradio app.
2.  Click the "Generate Meeting minutes" button.

Testing/CI
----------

No testing or CI configuration is present in this repository.

Deployment
-----------

This app can be deployed as a Hugging Face Space web app.

Contribution Notes
------------------

Contributions are welcome! Please follow standard GitHub practices for submitting pull requests and issues.

Limitations/TODOs (Inferred)
-----------------------------

*   The app assumes that the uploaded audio file is in a format supported by Google GenAI.
*   The meeting minutes generation model may not always produce accurate or complete results.
