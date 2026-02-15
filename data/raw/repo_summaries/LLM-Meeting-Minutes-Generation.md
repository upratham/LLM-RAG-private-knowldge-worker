<!-- Generated: 2026-02-15T02:58:58.437625Z | Model: gpt-4.1-nano -->

# LLM-Meeting-Minutes-Generation

## Overview
This repository provides a web application designed to generate structured meeting minutes from audio recordings. It leverages large language models and speech transcription services to produce comprehensive summaries, discussion points, takeaways, and action items in Markdown format. The project is suitable for organizations or individuals who want an automated solution for transforming meeting audio into organized documentation.

## Key Features
- Upload and process audio files (mp3, wav, m4a, etc.)
- Automatic transcription of audio using Google GenAI
- Generation of detailed meeting minutes including:
  - Summary with attendees, location, and date
  - Key discussion points
  - Action items with owners
- User-friendly web interface via Gradio
- Customizable models via environment variables

## Architecture / How it Works
The application workflow involves:
1. Uploading an audio file through the Gradio interface.
2. Uploading the audio to Google GenAI for transcription.
3. Sending the transcript to a Hugging Face Llama model for generating structured meeting minutes.
4. Streaming the generated minutes back to the user in real-time.

The core components include:
- `app.py`: Main application script managing the UI, transcription, and minutes generation.
- Environment variables for API keys (`HF_TOKEN`, `GOOGLE_API_KEY`) and model selection (`HF_MODEL`).
- External APIs: Google GenAI for speech-to-text, Hugging Face for language modeling.

## Notable Folders/Files
- `app.py`: Entry point of the application, contains the main logic for transcription and minutes generation.
- `notebooks/meeting_minutes.ipynb`: Presumably an original development or experimentation notebook.
- `requirements.txt` & `pyproject.toml`: Define dependencies needed for environment setup.
- `.gradio/`: Contains SSL certificates, indicating support for secure connections.
- `LICENSE`: MIT license, allowing broad reuse and modification.
- `README.md`: Documentation and instructions.

## Setup & Run
### Environment Setup
1. Clone the repository:
```bash
git clone https://github.com/upratham/LLM-Meeting-Minutes-Generation.git
cd LLM-Meeting-Minutes-Generation
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set required environment variables:
```bash
export HF_TOKEN='your-huggingface-api-token'
export GOOGLE_API_KEY='your-google-genai-api-key'
# Optional: specify model
export HF_MODEL='meta-llama/Llama-3.2-3B-Instruct'
```

### Running the Application
```bash
python app.py
```
This will start a local server, typically accessible at `http://127.0.0.1:7860/`. For deployment on Hugging Face Spaces, the app is configured to launch with sharing enabled.

## How to Use
1. Access the web interface.
2. Drag and drop an audio file (mp3, wav, m4a, etc.).
3. Click the "Generate Meeting minutes" button.
4. Wait for the app to process and stream the generated meeting minutes in Markdown format.
5. View or copy the structured minutes, including summary, discussion points, and action items.

## Testing / CI
There is no explicit mention of testing frameworks or CI/CD pipelines in the provided files. The project appears to be designed for deployment as a Hugging Face Space, which inherently supports sharing and testing via the web interface.

## Deployment
The presence of `.gradio/` certificates and the `app.py` script suggests that the application is intended to be deployed as a Hugging Face Space or similar hosting environment supporting Gradio apps. The `share=True` parameter in `demo.queue().launch()` indicates readiness for public sharing.

## Contribution Notes
No specific contribution guidelines are provided in the repository. For contributions, consider forking the repository, making improvements, and submitting pull requests.

## Limitations / TODOs (Inferred)
- **Model Customization:** The default model is `meta-llama/Llama-3.2-3B-Instruct`, but support for other models may require configuration.
- **Audio Format Support:** Only common audio formats are supported; unsupported formats may cause errors.
- **Streaming Response:** The minutes are streamed, which may have latency depending on the model and API response times.
- **Error Handling:** Basic error handling is present; more robust handling could improve user experience.
- **Localization:** Currently tailored for Denver council meetings; generalization to other meeting types may need adjustments.
- **Testing:** No automated tests are indicated; adding tests could improve reliability.

---

**Note:** If you need further details on specific components or configurations, please clarify or provide additional files or documentation.
