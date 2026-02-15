#!/usr/bin/env python3
"""
GitHub Repository Documentation Generator

Generates comprehensive documentation for GitHub repositories using OpenAI API.

Setup:
1. Set environment variables:
   - GITHUB_USERNAME: Your GitHub username
   - GITHUB_TOKEN: GitHub personal access token (optional, for higher rate limits)
   - OPENAI_API_KEY: OpenAI API key (required)

2. Run:
   python github_docs_generator.py

Output will be saved to: data/raw/repo_summaries/
"""

import os
import re
import json
import base64
import pathlib
import requests
from datetime import datetime
from openai import OpenAI
from tqdm import tqdm
from dotenv import load_dotenv

# Get project root directory (2 levels up from this file: src/github_docs/ -> project root)
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent.parent

# Load environment variables from .env file in project root
load_dotenv(PROJECT_ROOT / ".env")

# Configuration
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "").strip()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "").strip()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
MODEL_NAME = "gpt-4.1-nano"

OUT_DIR = PROJECT_ROOT / "data" / "raw" / "repo_summaries"

# Create output directory
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Processing limits
MAX_TREE_ITEMS = 800
MAX_FILE_CHARS = 12000
MAX_SOURCE_FILES = 12

IMPORTANT_FILES = [
    "README.md", "README.MD", "README.rst",
    "pyproject.toml", "requirements.txt", "Pipfile", "setup.py",
    "package.json", "pnpm-lock.yaml", "yarn.lock", "package-lock.json",
    "Cargo.toml", "go.mod", "pom.xml", "build.gradle", "build.gradle.kts",
    "Dockerfile", "docker-compose.yml",
    ".env.example", ".github/workflows",
    "Makefile", "compose.yaml",
]

SOURCE_EXTS = {
    ".py", ".js", ".ts", ".tsx", ".java", ".kt", ".go", ".rs", ".cpp", ".c", ".h", ".hpp",
    ".cs", ".php", ".rb", ".swift", ".scala", ".lua", ".sql", ".sh"
}


def gh_headers():
    """Generate GitHub API headers with optional authentication."""
    h = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return h


def gh_get(url, params=None):
    """Make authenticated GET request to GitHub API."""
    r = requests.get(url, headers=gh_headers(), params=params, timeout=60)
    r.raise_for_status()
    return r.json()


def list_repos(username):
    """Fetch all repos using pagination (100 per page)."""
    repos = []
    page = 1
    while True:
        batch = gh_get(
            f"https://api.github.com/users/{username}/repos",
            params={"per_page": 100, "page": page, "sort": "updated"}
        )
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos


def get_default_branch(repo_full_name, fallback="main"):
    """Get the default branch for a repository."""
    repo = gh_get(f"https://api.github.com/repos/{repo_full_name}")
    return repo.get("default_branch") or fallback


def get_repo_tree(repo_full_name, branch):
    """
    Get full recursive tree for a repository branch.
    Two-step process: get commit SHA from branch ref, then fetch full recursive tree.
    """
    ref = gh_get(f"https://api.github.com/repos/{repo_full_name}/git/refs/heads/{branch}")
    sha = ref["object"]["sha"]
    
    tree = gh_get(
        f"https://api.github.com/repos/{repo_full_name}/git/trees/{sha}",
        params={"recursive": 1}
    )
    return tree.get("tree", [])


def is_probably_binary(path):
    """Check file extension against known binary formats."""
    return any(path.lower().endswith(ext) for ext in [
        ".png", ".jpg", ".jpeg", ".gif", ".webp",
        ".pdf", ".zip", ".gz", ".7z",
        ".mp4", ".mov", ".avi",
        ".exe", ".dll", ".so", ".dylib"
    ])


def fetch_file_text(repo_full_name, path, branch):
    """
    Fetch and decode file content from GitHub API.
    GitHub API returns file content base64-encoded.
    Decode and handle both UTF-8 and Latin-1 encodings.
    """
    data = gh_get(
        f"https://api.github.com/repos/{repo_full_name}/contents/{path}",
        params={"ref": branch}
    )
    
    if isinstance(data, dict) and data.get("type") == "file":
        content = data.get("content", "")
        if data.get("encoding") == "base64" and content:
            raw = base64.b64decode(content.encode("utf-8", errors="ignore"))
            try:
                txt = raw.decode("utf-8", errors="replace")
            except Exception:
                txt = raw.decode("latin-1", errors="replace")
            return txt[:MAX_FILE_CHARS]
    return ""


def pick_key_files(tree_paths):
    """
    Multi-stage file selection:
    1. Important files (README, config, CI/CD)
    2. Source code files sorted by depth
    3. Deduplicate while preserving order
    """
    picked = []
    
    for imp in tqdm(IMPORTANT_FILES, desc="Finding important files"):
        for p in tree_paths:
            if p == imp or p.endswith("/" + imp) or (imp.endswith("/") and p.startswith(imp)):
                picked.append(p)

    src = [p for p in tree_paths if pathlib.Path(p).suffix in SOURCE_EXTS and not is_probably_binary(p)]
    src.sort(key=lambda x: (x.count("/"), len(x)))
    picked.extend(src[:MAX_SOURCE_FILES])

    seen, out = set(), []
    for p in tqdm(picked, desc="Deduplicating files"):
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def build_repo_context(repo, tree):
    """Build complete context for repository documentation generation."""
    repo_full = repo["full_name"]
    branch = get_default_branch(repo_full)

    tree_items = [t for t in tree if t.get("type") in ("blob", "tree")]
    tree_items = tree_items[:MAX_TREE_ITEMS]

    paths = [t["path"] for t in tree_items if "path" in t]
    files = [p for p in paths if not is_probably_binary(p)]

    chosen = pick_key_files(files)

    file_blobs = []
    for p in chosen:
        try:
            txt = fetch_file_text(repo_full, p, branch)
            if txt.strip():
                file_blobs.append({"path": p, "text": txt})
        except Exception:
            continue

    meta = {
        "name": repo.get("name"),
        "full_name": repo_full,
        "description": repo.get("description"),
        "topics": repo.get("topics", []),
        "default_branch": branch,
        "language": repo.get("language"),
        "updated_at": repo.get("updated_at"),
        "stargazers": repo.get("stargazers_count"),
        "forks": repo.get("forks_count"),
        "open_issues": repo.get("open_issues_count"),
        "license": (repo.get("license") or {}).get("spdx_id"),
        "html_url": repo.get("html_url"),
    }
    return meta, paths, file_blobs


def make_prompt(meta, paths, file_blobs):
    """Generate prompt for OpenAI API to create documentation."""
    tree_preview = "\n".join(paths[:600])

    def fence(path, text):
        ext = pathlib.Path(path).suffix.lstrip(".")
        lang = ext if ext else ""
        text = text[:MAX_FILE_CHARS]
        return f"### {path}\n```{lang}\n{text}\n```\n"

    snippets = "\n".join(fence(f["path"], f["text"]) for f in file_blobs[:20])

    return f"""
You are a senior engineer writing documentation.

Generate a SINGLE markdown document that explains this GitHub repository clearly.
Use proper headings and subheadings and keep it accurate based only on provided data.
If something is unclear, say so.

# Required structure
- Title with repo name
- Overview (what it is, who it's for)
- Key Features (bullets)
- Architecture / How it works (based on files/config)
- Notable folders/files (explain why they matter)
- Setup & Run (infer from configs; include commands if obvious)
- How to use (examples if you can infer)
- Testing / CI (if present)
- Deployment (if present)
- Contribution notes (if present)
- Limitations / TODOs you infer (clearly labeled as inference)

# Repo metadata (JSON)
{json.dumps(meta, indent=2)}

# File tree (preview)
{tree_preview}

# File excerpts
{snippets}
""".strip()


def safe_filename(name: str) -> str:
    """Replace invalid filename characters with underscores."""
    name = re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("_")
    return name or "repo"


def generate_markdown_with_openai(prompt: str) -> str:
    """Generate markdown documentation using OpenAI SDK."""
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is missing. Set it in your environment.")

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You write high-quality repo documentation in Markdown."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=4096,
        top_p=0.9,
    )

    return response.choices[0].message.content


def process_one_repo(repo):
    """Process a single repository and generate documentation."""
    repo_full = repo["full_name"]
    try:
        branch = get_default_branch(repo_full)
        tree = get_repo_tree(repo_full, branch)
        meta, paths, file_blobs = build_repo_context(repo, tree)
        prompt = make_prompt(meta, paths, file_blobs)
        md = generate_markdown_with_openai(prompt)

        out_path = OUT_DIR / f"{safe_filename(repo['name'])}.md"
        header = f"<!-- Generated: {datetime.utcnow().isoformat()}Z | Model: {MODEL_NAME} -->\n\n"
        out_path.write_text(header + md.strip() + "\n", encoding="utf-8")

        return {"repo": repo_full, "ok": True, "path": str(out_path)}
    except Exception as e:
        return {"repo": repo_full, "ok": False, "error": str(e)}


def main():
    """Fetch all repos and process with progress tracking."""
    # Validate required configuration
    if not GITHUB_USERNAME:
        raise RuntimeError("GITHUB_USERNAME environment variable is not set.")
    
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY environment variable is not set.")
    
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Output directory: {OUT_DIR}")
    print(f"Model: {MODEL_NAME}\n")

    repos = list_repos(GITHUB_USERNAME)
    print(f"Found {len(repos)} repos for @{GITHUB_USERNAME}")

    for repo in tqdm(repos, desc="Processing repositories"):
        result = process_one_repo(repo)
        if result["ok"]:
            print(f"✅ {result['repo']} -> {result['path']}")
        else:
            print(f"⚠️ {result['repo']} failed: {result['error']}")
    
    print(f"\n{'='*60}")
    print(f"Documentation saved to: {OUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
