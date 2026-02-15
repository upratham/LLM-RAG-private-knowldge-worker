<!-- Generated: 2026-02-15T02:59:08.335578Z | Model: gpt-4.1-nano -->

# LLM-Code-Explainer

## Overview
**LLM-Code-Explainer** is an AI-powered tool designed to help students understand code snippets. It runs locally using Ollama (an OpenAI-compatible API endpoint) combined with the OpenAI Python SDK. The application provides streaming explanations and features a user-friendly Gradio chat interface. It is suitable for learners seeking clear, step-by-step explanations of programming code.

## Key Features
- **Student-friendly code explanations:** Tailored responses to help learners grasp code concepts.
- **Streaming output:** Live, incremental responses mimicking real-time typing.
- **Local execution with Ollama:** Uses Ollama's API for local model inference at `http://localhost:11434/v1`.
- **Automatic prompt detection:** Detects if the user input is code and adjusts prompts accordingly.
- **Web UI via Gradio:** Interactive chat interface for easy usage and testing.

## Architecture / How It Works
The core of the application is a Python script (`app.py`) that:
- Loads environment variables for configuration.
- Sets up an OpenAI client pointing to a Hugging Face inference router, which proxies requests to the local Ollama server.
- Defines a system prompt to guide the AI's explanations.
- Implements a function to detect if user input resembles code.
- Uses the OpenAI chat completion API with streaming enabled to generate explanations.
- Serves the interface via Gradio's `ChatInterface`.

The repository leverages:
- `app.py` as the main application script.
- Environment variables for model and API configuration.
- `requirements.txt` and `pyproject.toml` for dependency management.
- Notebooks for development and testing purposes.

## Notable Folders/Files
- **`app.py`**: Main script that runs the Gradio chat interface and handles API interactions.
- **`notebooks/`**: Contains Jupyter notebooks used during development or experimentation.
- **`.gradio/`**: Stores SSL certificates for secure deployment if needed.
- **`requirements.txt` & `pyproject.toml`**: Manage dependencies required for the application.
- **`LICENSE`**: Specifies the MIT license under which the project is released.
- **`README.md`**: Provides project overview, setup instructions, and usage details.

## Setup & Run
### 1) Install and Start Ollama
```bash
ollama serve
# In another terminal, pull the desired model
ollama pull llama3.2
```

### 2) Create Virtual Environment and Install Dependencies
```bash
python -m venv .venv
# Activate the environment:
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 3) Configure Model and Endpoint
Set environment variables or modify the code:
```python
# In app.py or environment:
# For local Ollama server:
OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL_LLAMA = "llama3.2"  # or specify a different model if available
```

### 4) Run the Application
```bash
python app.py
```

## How to Use
- Access the local Gradio interface (usually at `http://localhost:7860`).
- Type or paste a code snippet or a question about code.
- The system automatically detects if the input is code and adjusts the explanation prompt.
- View the streaming explanation as the AI responds in real-time.
- Example:
  - Input: `def add(a, b): return a + b`
  - The AI will explain what this function does and how it works.

## Testing / CI
- No explicit testing or CI configurations are mentioned in the provided files.
- Development notebooks in `notebooks/` suggest manual testing during development.

## Deployment
- The primary deployment method is via Gradio's `launch()` function.
- For public sharing, the app can be hosted on Hugging Face Spaces or similar platforms supporting Gradio.
- SSL certificates are stored in `.gradio/`, indicating potential for secure deployment.

## Contribution Notes
- No specific contribution guidelines are provided in the repository.
- Users are encouraged to fork, modify, and improve the code, adhering to the MIT license.

## Limitations / TODOs (Inferred)
- **Model dependency:** Relies on Ollama and specific models (`llama3.2`), which may require local setup.
- **Input detection accuracy:** The heuristic for detecting code snippets may not be perfect.
- **Performance considerations:** Streaming responses may be slow with large models or limited hardware.
- **Extensibility:** Currently tailored for code explanation; adapting for other tasks may require modifications.
- **Documentation:** Additional usage examples, customization options, and deployment instructions could enhance usability.

---

*Note: If you need further details on specific configurations or code behavior, please specify.*
