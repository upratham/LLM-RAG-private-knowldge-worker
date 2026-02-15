<!-- Generated: 2026-02-15T01:23:39.207479Z | Model: llama3.1 -->

**LLM-Debate-Competition**
==========================

Overview
--------

The LLM-Debate-Competition is a multi-agent debate simulator built in Python. It allows for a "debate competition" between two Large Language Model (LLM) competitors, each with their own system prompt/persona, and optionally uses a third "supervisor/judge" agent to evaluate and score the round.

Key Features
------------

*   Multi-agent debate simulator with optional judge scoring
*   Supports local LLMs via Ollama or OpenAI API
*   Designed for Jupyter Notebook interface
*   Customizable debate topics, competitor system prompts, and supervisor/judge prompt

Architecture / How it Works
---------------------------

The project is structured as follows:

*   `Debate_Competittion.ipynb`: Main demo/runner notebook
*   `pyproject.toml`: Project metadata + dependency wiring
*   `requirements.txt`: Runtime dependencies

Notable Folders/Files
----------------------

*   `.gitignore`: Git ignore file to exclude unnecessary files from version control
*   `LICENSE`: License file (MIT)
*   `README.md`: This documentation file
*   `pyproject.toml`: Project metadata + dependency wiring
*   `requirements.txt`: Runtime dependencies

Setup & Run
------------

### Prerequisites

*   Python 3.11.x
*   Virtual environment tool (`venv`, `conda`, etc.)
*   Ollama installed and running (if using local LLMs)

### Setup

1.  Clone the repository: `git clone https://github.com/upratham/LLM-Debate-Competition.git`
2.  Create and activate a virtual environment: `python -m venv .venv` (Windows) or `source .venv/bin/activate` (macOS/Linux)
3.  Install dependencies: `pip install -r requirements.txt`

### Configuration

*   Using Ollama (local): Update the notebook to use an OpenAI-compatible base URL like `http://localhost:11434/v1`
*   Using OpenAI: Create a `.env` file and set `OPENAI_API_KEY="your_api_key_here"`

How to Use
------------

### Run via Jupyter Notebook

1.  Open `Debate_Competittion.ipynb` in Jupyter Notebook
2.  Run cells from top to bottom

Customization
-------------

*   Edit the debate topic, competitor system prompts, and supervisor/judge prompt as needed

Testing / CI
------------

No testing or CI information is provided.

Deployment
----------

No deployment information is provided.

Contribution Notes
------------------

PRs welcome. If making changes:

1.  Keep prompts readable and safe for general audiences.
2.  Prefer small, focused commits.
3.  Add a short note to the README if behavior changes.

Limitations / TODOs
--------------------

*   Turn notebook into a CLI app (`python -m debate_competition ...`)
*   Add deterministic scoring schema + validation
*   Store transcripts and scores under `/runs/`
*   Add unit tests for formatting + evaluation parsing
*   Support more competitors / tournament brackets

Author
------

Maintained by **Prathamesh Uravane**  
Email: [upratham2002@gmail.com](mailto:upratham2002@gmail.com)
