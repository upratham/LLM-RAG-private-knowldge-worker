<!-- Generated: 2026-02-15T02:59:47.129200Z | Model: gpt-4.1-nano -->

# LLM-AI-Company-Brochure-Generator

## Overview
The **LLM-AI-Company-Brochure-Generator** is a Python-based project designed to automate the creation of sales brochures for companies by scraping website content and generating professional marketing materials using large language models (LLMs). It supports both cloud-based models like **Google Gemini** and local models via **Ollama**. This tool is suitable for marketers, content creators, and developers interested in automating brochure generation with AI.

## Key Features
- **Website Content Scraping:** Utilizes `BeautifulSoup` to extract and clean website data.
- **AI-Driven Brochure Generation:** Uses LLMs such as Google Gemini or local Ollama models to produce marketing brochures.
- **Support for Multiple LLMs:** Seamless integration with cloud-based Gemini API and local Ollama models.
- **Jupyter Notebook Interface:** Provides notebooks for easy interaction and customization.
- **Pythonic and Modular Design:** Clear project structure with dedicated scripts and configuration files.

## Architecture / How it Works
The project primarily revolves around scraping website content and feeding it into an LLM for brochure creation. The key components include:
- **`scraper.py`:** Handles website content extraction and link retrieval.
- **Jupyter Notebooks (`Brochure_Generater_Gemini.ipynb` and `Brochure_Generater_ollama.ipynb`):** Orchestrate the process of fetching content, calling the respective LLM API, and generating the brochure.
- **Configuration Files:** Manage dependencies (`requirements.txt`, `pyproject.toml`) and environment variables (`.env`).

The notebooks likely contain the logic to:
1. Fetch website content using `scraper.py`.
2. Send the content to the chosen LLM API (Gemini or Ollama).
3. Receive generated brochure content.
4. Display or save the output.

## Notable Folders/Files
- **`scraper.py`:** Contains functions for scraping website titles, text, and links.
- **`Brochure_Generater_Gemini.ipynb`:** Notebook for generating brochures using Google Gemini API.
- **`Brochure_Generater_ollama.ipynb`:** Notebook for generating brochures using local Ollama models.
- **`.gradio/`:** Contains SSL certificates, indicating a possible Gradio interface for user interaction.
- **`requirements.txt` & `pyproject.toml`:** Manage project dependencies.
- **`.env`:** Environment variables, notably for API keys.

## Setup & Run
### Prerequisites
- Python 3.11.x
- Git
- Internet connection (for Gemini API)
- Ollama installed and configured (for local models)
- Sufficient RAM (~8 GB recommended for Ollama)

### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/upratham/LLM-AI-Company-Brochure-Generator.git
cd LLM-AI-Company-Brochure-Generator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Obtain API Keys
- **Google Gemini:**
  1. Visit [Google AI Studio](https://aistudio.google.com/)
  2. Sign in and generate an API key.
  3. Add the key to `.env` as `GEMINI_API_KEY`.

- **Ollama:**
  1. Download from [https://ollama.com/download](https://ollama.com/download)
  2. Verify installation with `ollama --version`.
  3. Pull desired models:
     ```bash
     ollama pull llama3
     ```

### Running the Notebooks
- **Using Gemini (Cloud):**
```bash
jupyter notebook Brochure_Generater_Gemini.ipynb
```

- **Using Ollama (Local):**
```bash
jupyter notebook Brochure_Generater_ollama.ipynb
```

Ensure Ollama is running and models are pulled before executing.

## How to Use
### Scraping Website Content
In the notebooks, you can specify a URL to scrape:
```python
from scraper import fetch_website_contents

content = fetch_website_contents("https://example.com")
print(content)
```

### Generating Brochures
Within the notebooks:
- Input the scraped content.
- Select the LLM API (Gemini or Ollama).
- Run the cells to generate a brochure, which will be displayed or saved.

### Example Workflow
1. Scrape website:
```python
content = fetch_website_contents("https://companywebsite.com")
```
2. Generate brochure via notebook cell:
```python
brochure_text = generate_brochure(content)
print(brochure_text)
```

*(Note: Actual function names depend on notebook implementation)*

## Testing / CI
No explicit testing or CI configurations are mentioned in the provided data.

## Deployment
No specific deployment instructions are provided. The project appears to be designed for local or notebook-based execution.

## Contribution Notes
No contribution guidelines are included in the provided data.

## Limitations / TODOs (Inferred)
- **Limited error handling:** The scraper and API calls may need more robust error management.
- **Batch processing:** Currently, it seems focused on single website scraping; batch or multi-website processing could be a future enhancement.
- **Brochure formatting:** The output is likely plain text; adding PDF export or styled formatting could improve usability.
- **Multi-language support:** Not mentioned; currently likely English-only.
- **UI/UX:** The presence of `.gradio/` suggests potential for a web interface, but details are not provided.

---

**Note:** For detailed usage, refer to the individual notebooks and the `scraper.py` script. If further clarification is needed, especially regarding the internal logic of the notebooks, please specify.
