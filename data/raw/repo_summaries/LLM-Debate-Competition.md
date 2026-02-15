<!-- Generated: 2026-02-15T03:00:40.506121Z | Model: gpt-4.1-nano -->

# LLM-Debate-Competition

## Overview
The **LLM-Debate-Competition** repository is a lightweight multi-agent debate simulator built in Python. It enables two large language model (LLM) agents to engage in a structured debate on a specified topic, each representing different stances or personas. An optional third agent acts as a judge or supervisor, evaluating the debate and providing structured feedback or scoring. The primary interface is a Jupyter Notebook, making it accessible for experimentation and demonstration.

This project is suitable for AI researchers, developers, or enthusiasts interested in multi-agent interactions, prompt engineering, or evaluating LLM capabilities in argumentation and reasoning.

---

## Key Features
- Simulates a debate between two LLM-based competitors, each with customizable prompts and personas.
- Responses are formatted in clean Markdown, including headings and concise arguments.
- An optional judge/supervisor agent can review the debate and output structured evaluations (e.g., JSON scores).
- Supports both local LLMs via Ollama and cloud-based OpenAI API.
- Designed for easy customization of debate topics, personas, and evaluation criteria.
- Interactive demonstration via Jupyter Notebook.

---

## Architecture / How it Works
The core functionality is implemented within a Jupyter Notebook (`Debate_Competittion.ipynb`). The notebook orchestrates the debate flow by:

1. Initializing two competitor agents with their respective prompts and personas.
2. Alternating turns where each agent generates responses based on the debate history.
3. Formatting responses in Markdown for clarity.
4. Optionally invoking a judge agent to evaluate the debate, which can be configured to use either:
   - Local LLMs via Ollama (by setting the base URL and models)
   - OpenAI API (by setting the API key)
   
The system relies on Python scripts and dependencies specified in `pyproject.toml` and `requirements.txt` to handle API calls, environment management, and response formatting.

---

## Notable Folders/Files
- **`Debate_Competittion.ipynb`**: The main interactive notebook for running debates, customizing prompts, and viewing results.
- **`pyproject.toml`**: Contains project metadata and dependency specifications.
- **`requirements.txt`**: Lists runtime dependencies for environment setup.
- **`.gitignore`**: Specifies files to ignore in version control.
- **`LICENSE`**: Presumably contains the MIT license (not shown here).
- **`README.md`**: The current documentation file.

---

## Setup & Run
### Prerequisites
- Python 3.11.x installed.
- Virtual environment tool (recommended: `venv` or `conda`).
- Optional: Ollama installed and running if using local models.

### Setup Steps
1. Clone the repository:
```bash
git clone https://github.com/upratham/LLM-Debate-Competition.git
cd LLM-Debate-Competition
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# Windows:
# .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration
- **Using Ollama (local models):**
  - Ensure Ollama is installed and running.
  - Pull models:
    ```bash
    ollama pull llama3.2
    ollama pull llama3.1
    ```
  - Set the base URL in the notebook if needed (`http://localhost:11434/v1`).

- **Using OpenAI API:**
  - Create a `.env` file with your API key:
    ```bash
    OPENAI_API_KEY="your_api_key_here"
    ```
  - The notebook will automatically use this key for API calls.

---

## How to Use
1. Launch Jupyter Notebook:
```bash
jupyter notebook
```
2. Open `Debate_Competittion.ipynb`.
3. Run cells sequentially to:
   - Configure debate parameters (topic, prompts, number of rounds).
   - Initiate the debate simulation.
   - Review the generated debate transcript and evaluation scores.

### Customization
- Modify the **topic** variable to set the debate subject.
- Adjust the **system prompts** for each competitor to change personas or constraints.
- Change the **judge prompt** to alter evaluation criteria and scoring.

---

## Testing / CI
No explicit testing or CI setup is mentioned in the provided files or description. Future improvements could include adding unit tests for response formatting and evaluation parsing.

---

## Deployment
Currently, the project is designed for local experimentation within a Jupyter Notebook environment. There is no mention of deployment scripts or cloud deployment procedures.

---

## Contribution Notes
- Contributions are welcome via pull requests.
- When modifying prompts or logic, ensure clarity and safety.
- Keep commits small and focused.
- Update the README if significant behavior or feature changes are introduced.

---

## Limitations / TODOs (Inferred)
- The project currently relies heavily on manual configuration within the notebook.
- No automated testing or validation of debate quality or scoring.
- Future enhancements could include:
  - Turning the notebook into a command-line interface (`CLI`).
  - Adding persistent storage for debate transcripts and scores.
  - Implementing more sophisticated scoring schemas.
  - Supporting multiple debate rounds or tournament structures.
  - Adding unit tests for core formatting and evaluation functions.

---

## Author
Maintained by **Prathamesh Uravane**  
Email: [upratham2002@gmail.com](mailto:upratham2002@gmail.com)

---

*Note: Some details, such as the exact implementation of the debate flow or scoring schema, are inferred from the provided files and descriptions. For precise behavior, review the `Debate_Competittion.ipynb` directly.*
