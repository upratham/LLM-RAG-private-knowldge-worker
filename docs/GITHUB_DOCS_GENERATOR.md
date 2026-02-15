# GitHub Documentation Generator

The GitHub Documentation Generator is an automated tool that creates comprehensive, AI-powered documentation for GitHub repositories. It analyzes repository structure, configurations, and source code to generate detailed markdown documentation.

## Overview

This tool fetches repositories from a GitHub account, analyzes their content, and uses OpenAI's API to generate structured, informative documentation. The generated documentation follows a consistent format and provides insights into:

- Project overview and purpose
- Key features and architecture
- Setup and installation instructions
- Usage examples and API documentation
- Testing and deployment information

## Features

- **Automated Repository Discovery**: Fetches all repositories for a given GitHub user
- **Intelligent File Selection**: Prioritizes important files (README, configs, source code)
- **AI-Powered Documentation**: Uses OpenAI models to generate comprehensive docs
- **Structured Output**: Consistent markdown format with proper sections
- **Progress Tracking**: Real-time progress updates with detailed status
- **Configurable Limits**: Control processing scope and API usage
- **Error Handling**: Graceful handling of API failures and edge cases

## Setup

### Prerequisites

1. **Python 3.8+** with virtual environment
2. **GitHub Account** (for accessing repositories)
3. **OpenAI API Key** (for documentation generation)
4. **GitHub Personal Access Token** (optional, for higher rate limits)

### Environment Variables

Add the following to your `.env` file in the project root:

```env
# Required
GITHUB_USERNAME=your_github_username
OPENAI_API_KEY=your_openai_api_key

# Optional (increases GitHub API rate limits)
GITHUB_TOKEN=your_github_personal_access_token
```

### Getting API Keys

**GitHub Personal Access Token:**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo` (for private repos) or `public_repo` (for public only)
4. Copy the generated token

**OpenAI API Key:**
1. Visit https://platform.openai.com/api-keys
2. Create new API key
3. Copy and save securely

## Usage

### Basic Usage

Navigate to your project directory and run:

```bash
# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows

# Run the generator
python src/github_docs/github_docs_generator.py
```

### Output

Generated documentation files are saved to:
```
data/raw/repo_summaries/
├── repository-1.md
├── repository-2.md
└── repository-3.md
```

## Configuration

### Model Settings

The generator uses the following configuration (defined in `github_docs_generator.py`):

```python
MODEL_NAME = "gpt-4.1-nano"           # OpenAI model for documentation
MAX_TREE_ITEMS = 800                   # Maximum repository tree items to process
MAX_FILE_CHARS = 12000                 # Maximum characters per file
MAX_SOURCE_FILES = 12                  # Maximum source code files to analyze
```

### File Selection Priority

The generator intelligently selects files in this order:

1. **Important Files** (highest priority):
   - README files (README.md, README.rst)
   - Package configuration (pyproject.toml, package.json, requirements.txt, etc.)
   - Dependency locks (yarn.lock, Pipfile, pom.xml, etc.)
   - Docker files (Dockerfile, docker-compose.yml)
   - CI/CD configurations (.github/workflows, Makefile)

2. **Source Code Files** (by directory depth):
   - Python (.py)
   - JavaScript/TypeScript (.js, .ts, .tsx)
   - Java/Kotlin (.java, .kt)
   - Go (.go)
   - Rust (.rs)
   - C/C++ (.c, .cpp, .h, .hpp)
   - Other languages (.cs, .php, .rb, .swift, .scala, .lua, .sql, .sh)

### Configuration in config.json

Update `config/config.json` to customize settings:

```json
{
  "github_docs": {
    "model": "gpt-4.1-nano",
    "max_tree_items": 800,
    "max_file_chars": 12000,
    "max_source_files": 12,
    "output_dir": "./data/raw/repo_summaries"
  }
}
```

## Documentation Structure

Generated documentation follows this structure:

1. **Title**: Repository name and description
2. **Overview**: What the project is and who it's for
3. **Key Features**: Bullet-point feature list
4. **Architecture**: How the system works (based on code analysis)
5. **Notable Folders/Files**: Important directories explained
6. **Setup & Run**: Installation and execution instructions
7. **Usage Examples**: How to use the project
8. **Testing**: Test suite and CI information (if present)
9. **Deployment**: Deployment instructions (if present)
10. **Contributing**: Contribution guidelines (if present)
11. **Limitations**: Inferred limitations and TODOs

## API Usage

### GitHub API

The generator makes the following GitHub API calls per repository:

1. **List Repositories**: `GET /users/{username}/repos` (paginated)
2. **Get Repository**: `GET /repos/{owner}/{repo}`
3. **Get Branch Reference**: `GET /repos/{owner}/{repo}/git/refs/heads/{branch}`
4. **Get Tree**: `GET /repos/{owner}/{repo}/git/trees/{sha}?recursive=1`
5. **Get File Contents**: `GET /repos/{owner}/{repo}/contents/{path}` (per file)

**Rate Limits:**
- Without token: 60 requests/hour
- With token: 5,000 requests/hour

### OpenAI API

The generator makes one API call per repository:

- **Model**: gpt-4.1-nano (or configured model)
- **Max Tokens**: 4,096
- **Temperature**: 0.2
- **Estimated Cost**: ~$0.001-0.01 per repository (varies by model)

## Performance

### Processing Time

Average processing time per repository:
- Small repos (<50 files): 10-15 seconds
- Medium repos (50-200 files): 15-30 seconds
- Large repos (>200 files): 30-60 seconds

### Optimization Tips

1. **Reduce API Calls**: Use GitHub token to avoid rate limiting
2. **Adjust Limits**: Lower `MAX_SOURCE_FILES` for faster processing
3. **Batch Processing**: Process multiple repos in sequence (already implemented)
4. **Skip Processed**: Manually skip repos that already have documentation

## Troubleshooting

### Common Issues

**1. RuntimeError: GITHUB_USERNAME environment variable is not set**

**Solution**: Add `GITHUB_USERNAME` to your `.env` file:
```env
GITHUB_USERNAME=your_github_username
```

**2. RuntimeError: OPENAI_API_KEY is missing**

**Solution**: Add `OPENAI_API_KEY` to your `.env` file:
```env
OPENAI_API_KEY=sk-...your-key
```

**3. GitHub API Rate Limit Exceeded**

**Solution**: Add GitHub personal access token to `.env`:
```env
GITHUB_TOKEN=ghp_...your-token
```

**4. OpenAI API Error: Insufficient Quota**

**Solution**: Check your OpenAI account billing and add credits.

**5. ModuleNotFoundError: No module named 'openai'**

**Solution**: Activate virtual environment and install dependencies:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**6. Empty or Incomplete Documentation**

**Possible Causes:**
- Repository is empty or has minimal content
- API token has insufficient permissions
- Rate limits exceeded

**Solution**: Check repository content and API credentials.

## Code Structure

### Main Functions

```python
# GitHub API Interactions
gh_get(url, params=None)                    # Make authenticated GitHub API request
list_repos(username)                        # Fetch all repositories for user
get_default_branch(repo_full_name)          # Get default branch name
get_repo_tree(repo_full_name, branch)       # Get repository file tree

# File Processing
fetch_file_text(repo_full_name, path, branch)  # Fetch and decode file content
pick_key_files(tree_paths)                     # Select important files
is_probably_binary(path)                       # Check if file is binary

# Documentation Generation
build_repo_context(repo, tree)              # Build context for AI prompt
make_prompt(meta, paths, file_blobs)        # Generate AI prompt
generate_markdown_with_openai(prompt)       # Call OpenAI API
process_one_repo(repo)                      # Process single repository

# Main Entry Point
main()                                      # Process all repositories
```

## Integration with RAG System

The generated documentation can be used as knowledge base input for the RAG system:

```python
from src.rag_system import RAGSystem

# Initialize RAG system
rag = RAGSystem(config_path='./config/config.json')

# Ingest generated documentation
rag.ingest_documents('./data/raw/repo_summaries')

# Build index
rag.build_index()

# Query about your repositories
response = rag.query("How does the authentication work in my project?")
print(response['response'])
```

## Advanced Usage

### Custom Model Selection

Modify the model in the script:

```python
MODEL_NAME = "gpt-4"  # Use GPT-4 for higher quality
# or
MODEL_NAME = "gpt-3.5-turbo"  # Use GPT-3.5 for lower cost
```

### Processing Specific Repositories

Modify the main function to filter repositories:

```python
def main():
    repos = list_repos(GITHUB_USERNAME)
    
    # Filter by name
    repos = [r for r in repos if "important" in r["name"].lower()]
    
    # Or filter by language
    repos = [r for r in repos if r.get("language") == "Python"]
    
    # Process filtered repos
    for repo in tqdm(repos, desc="Processing repositories"):
        result = process_one_repo(repo)
        # ...
```

### Parallel Processing

For processing many repositories faster, consider implementing parallel processing:

```python
from concurrent.futures import ThreadPoolExecutor

def main():
    repos = list_repos(GITHUB_USERNAME)
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_one_repo, repos))
```

**Note**: Be mindful of GitHub and OpenAI API rate limits when using parallel processing.

## Best Practices

1. **Start Small**: Test with a few repositories first
2. **Monitor Costs**: Track OpenAI API usage and costs
3. **Version Control**: Commit generated docs to track changes
4. **Review Output**: AI-generated docs may need human review
5. **Update Regularly**: Regenerate docs when repositories change
6. **Use Tokens**: Always use GitHub token for better rate limits

## Limitations

- **AI Limitations**: Generated documentation depends on AI model quality
- **API Costs**: Processing many large repositories can be expensive
- **Rate Limits**: GitHub and OpenAI APIs have usage limits
- **Binary Files**: Cannot analyze binary files (images, executables)
- **Private Repos**: Requires GitHub token with appropriate permissions
- **Large Repos**: Very large repositories may exceed processing limits

## Future Enhancements

- [ ] Support for multiple GitHub accounts
- [ ] Incremental updates (only regenerate changed repos)
- [ ] Custom documentation templates
- [ ] Integration with other LLM providers
- [ ] Web UI for configuration and monitoring
- [ ] Scheduled automatic updates
- [ ] Documentation quality metrics
- [ ] Multi-language support for non-English repos

## Contributing

To improve the GitHub Documentation Generator:

1. Fork the repository
2. Create a feature branch
3. Make your changes to `src/github_docs/github_docs_generator.py`
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

## Support

For issues and questions:
- Check this documentation first
- Review error messages carefully
- Verify environment variables and API keys
- Check API rate limits and quotas
- Open an issue on GitHub with detailed information

## License

This tool is part of the RAG LLM Private Knowledge Worker project and follows the same MIT License.

---

**Last Updated**: February 2026
