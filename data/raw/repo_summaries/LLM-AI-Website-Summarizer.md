<!-- Generated: 2026-02-15T03:00:07.610298Z | Model: gpt-4.1-nano -->

# LLM-AI-Website-Summarizer

## Overview
The **LLM-AI-Website-Summarizer** is a Python-based project designed to extract and summarize the content of any webpage. It leverages large language models (LLMs) via the OpenAI API or a local Ollama instance, providing flexible options for cloud-based or local processing. The project is intended for developers, researchers, or AI enthusiasts interested in web scraping, natural language processing, and summarization tasks.

## Key Features
- Web scraping using `requests` and `BeautifulSoup`.
- Supports summarization through OpenAI's cloud API or a local Ollama server.
- Includes Jupyter notebooks for interactive usage:
  - `summerizer_Openai.ipynb` for cloud-based summarization.
  - `summerizer_Ollama.ipynb` for local model summarization.
- Easy setup with dependency management via `pip`.
- Environment variable configuration for API keys.
- Modular design allowing for model swapping and customization.

## Architecture / How It Works
The repository primarily consists of Jupyter notebooks that perform the following steps:
1. **Web Scraping:** Fetch webpage content using `requests` and parse it with `BeautifulSoup`.
2. **Summarization:** Send the extracted text to either:
   - OpenAI's API (`openai` SDK) for cloud-based models.
   - A local Ollama server configured to serve models compatible with OpenAI's API.
3. **Model Interaction:** Use the `openai` Python SDK to communicate with the chosen model endpoint, passing the webpage content for summarization.

The notebooks contain helper functions, notably `summarize(url)`, which streamline the process.

## Notable Folders/Files
- `summerizer_Gemini.ipynb`: Presumably another summarization notebook, possibly using a different model or approach (not explicitly described).
- `summerizer_Ollama.ipynb`: Notebook for local Ollama-based summarization.
- `summerizer_Openai.ipynb`: Notebook for cloud OpenAI API summarization.
- `pyproject.toml`: Defines project dependencies, indicating a comprehensive environment for NLP and ML tasks.
- `requirements.txt`: Lists essential packages like `openai`, `beautifulsoup4`, and `requests`.
- `.gitignore`: Ensures sensitive files like `.env` are not committed.
- `LICENSE`: MIT License, allowing broad reuse.

## Setup & Run
### Prerequisites
- Python 3.10+ (recommended based on dependencies)
- Jupyter Notebook or Jupyter Lab

### Installing Dependencies
Create and activate a virtual environment:

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
# .venv\Scripts\Activate.ps1
```

Upgrade pip and install dependencies:

```bash
pip install -U pip
pip install -U openai python-dotenv beautifulsoup4 requests ipython jupyter
```

### Running the Notebooks
Start Jupyter:

```bash
jupyter lab
# or
jupyter notebook
```

Open either `summerizer_Openai.ipynb` or `summerizer_Ollama.ipynb` to begin.

## How to Use
### Using OpenAI API (Cloud)
1. Obtain an API key:
   - Sign in at [OpenAI Platform](https://platform.openai.com/account/api-keys).
   - Create a new secret key.
2. Save the key in a `.env` file in the project root:

```bash
# .env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

3. Run the `summerizer_Openai.ipynb` notebook:
   - It loads the API key via `python-dotenv`.
   - Use the `summarize(url)` function to fetch and summarize any webpage.

### Using Ollama (Local)
1. Install Ollama:
   - Follow [Ollama docs](https://docs.ollama.com/) for your OS.
2. Start Ollama server:
   - For macOS/Windows: it runs in the background post-installation.
   - For Linux: run `ollama serve`.
3. Pull a model (default is `llama3.2`):

```bash
ollama pull llama3.2
```

4. Configure the notebook:
   - Set `OLLAMA_BASE_URL` to `http://localhost:11434/v1`.
   - Use `OpenAI` SDK with the `base_url` pointing to Ollama.
5. Run `summerizer_Ollama.ipynb` and call `summarize(url)`.

## Testing / CI
No explicit testing or CI configurations are mentioned in the provided data. The focus appears to be on notebooks and setup instructions.

## Deployment
No specific deployment procedures are described. The project is primarily designed for local or notebook-based usage.

## Contribution Notes
No contribution guidelines are provided in the current documentation.

## Limitations / TODOs (Inferred)
- **Limited to notebook-based interaction:** No CLI or API server is described.
- **Model flexibility:** Currently supports only specified models (`llama3.2` for Ollama, default models for OpenAI).
- **Security:** Users must ensure `.env` files are kept secret; no mention of secret management beyond `.env`.
- **Potential for expansion:** Could include CLI tools, automated scripts, or deployment pipelines in future iterations.

---

**For further details, refer to the [GitHub repository](https://github.com/upratham/LLM-AI-Website-Summarizer).**
