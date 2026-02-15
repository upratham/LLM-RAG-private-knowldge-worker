<!-- Generated: 2026-02-15T01:18:10.316591Z | Model: llama3.1 -->

**LLM-AI-Website-Summarizer**
==========================

Overview
--------

This repository provides a tool to summarize any webpage using either OpenAI API or local Ollama models. The project includes three Jupyter notebooks: `summerizer_Openai.ipynb`, `summerizer_Ollama.ipynb`, and `summerizer_Gemini.ipynb`. Each notebook uses a different approach to summarize web content.

Key Features
------------

*   Summarize any webpage using OpenAI API or local Ollama models.
*   Web scraping with `requests` + `BeautifulSoup`.
*   A small summarization helper (`summarize(url)`) in each notebook.
*   Model calls via the **OpenAI Python SDK** (`from openai import OpenAI`).

Architecture / How it works
---------------------------

The project uses a combination of web scraping and model-based summarization. The `summerizer_Openai.ipynb` notebook uses the OpenAI API to summarize web content, while the `summerizer_Ollama.ipynb` notebook uses local Ollama models.

Notable Folders/Files
----------------------

*   `.env`: stores API keys securely.
*   `pyproject.toml`: defines project dependencies and settings.
*   `requirements.txt`: lists project dependencies.

Setup & Run
------------

### Prerequisites

*   Python **3.10+**
*   Jupyter (Notebook or Lab)

### Install Dependencies

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -U pip
```

Install packages:

```bash
pip install -U openai python-dotenv beautifulsoup4 requests ipython jupyter
```

### Run the Notebooks

Start Jupyter:

```bash
jupyter lab
# or: jupyter notebook
```

Then open either:

*   `summerizer_Openai.ipynb`
*   `summerizer_Ollama.ipynb`

How to Use
------------

1.  Choose a notebook (`summerizer_Openai.ipynb` or `summerizer_Ollama.ipynb`) and run it.
2.  Update the `model=` value if you want to use a different OpenAI model (for OpenAI API).
3.  For Ollama, ensure Ollama is running on `http://localhost:11434`.

Testing / CI
-------------

No testing or CI scripts are present in this repository.

Deployment
----------

No deployment scripts are present in this repository.

Contribution Notes
------------------

Contributions are welcome! Please follow the standard GitHub workflow for submitting pull requests and issues.

Limitations / TODOs (Inferred)
-------------------------------

*   The project assumes a stable internet connection for OpenAI API calls.
*   Ollama setup requires manual installation and configuration.
*   No error handling is implemented for potential exceptions during web scraping or model calls.

**Note:** Some information, such as the `pyproject.toml` file, was not explicitly mentioned in the provided data. However, based on the context, it appears to be a project dependencies file.
