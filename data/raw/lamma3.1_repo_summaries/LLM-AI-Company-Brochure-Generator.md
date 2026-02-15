<!-- Generated: 2026-02-15T00:45:31.958664Z | Model: llama3.1 -->

Here is the Markdown document that explains this GitHub repository clearly:

**LLM-AI-Company-Brochure-Generator**
=====================================

Overview
--------

This project, **LLM-AI-Company-Brochure-Generator**, is an AI-powered company sales brochure generator. It scrapes website content and generates professional marketing brochures using LLMs such as Google Gemini or local Ollama models.

Key Features
-------------

* Website content scraping using `BeautifulSoup`
* AI brochure generation
* Supports both cloud-based (Gemini) and local (Ollama) LLM workflows

Architecture / How it works
---------------------------

The project consists of the following components:

* `scraper.py`: This script fetches website content and extracts hyperlinks.
* `Brochure_Generater_Gemini.ipynb` and `Brochure_Generater_ollama.ipynb`: These Jupyter notebooks use LLMs to generate brochures. The Gemini notebook uses the Google Gemini API, while the Ollama notebook uses local Ollama models.

Notable folders/files
----------------------

* `.gradio/`: This folder contains Gradio-related files.
* `LICENSE`: This is the project's license file.
* `pyproject.toml` and `requirements.txt`: These files manage dependencies for the project.

Setup & Run
------------

To set up the project, follow these steps:

1. Clone the repository using `git clone https://github.com/upratham/LLM-AI-Company-Brochure-Generator.git`.
2. Create a virtual environment using `python -m venv venv` (on Windows) or `source venv/bin/activate` (on macOS/Linux).
3. Install dependencies using `pip install -r requirements.txt` or `pip install .` (using `pyproject.toml`).

To run the project, follow these steps:

* For Gemini: Open and run `Brochure_Generater_Gemini.ipynb`.
* For Ollama: Open and run `Brochure_Generater_ollama.ipynb`.

How to use
------------

To use the scraper, import it in your Python script:
```python
from scraper import fetch_website_contents
```
Then call the function with a URL as an argument:
```python
content = fetch_website_contents("https://example.com")
print(content)
```

Testing / CI
-------------

There is no explicit testing or CI setup for this project.

Deployment
----------

This project does not have any deployment instructions.

Contribution notes
------------------

Contributions are welcome! Please follow the standard GitHub workflow for contributing to open-source projects.

Limitations / TODOs
--------------------

* Inference: The project seems to be missing some features, such as PDF brochure export and multi-language brochure generation. These might be planned for future enhancements.
* Code organization: The code is not well-organized, with multiple notebooks and scripts scattered throughout the repository. A more structured approach would improve maintainability.

Note: This documentation is based on the provided data and may not cover all aspects of the project.
