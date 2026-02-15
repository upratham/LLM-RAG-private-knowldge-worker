# Makefile - Useful development commands

.PHONY: help install dev-install test lint format clean run docs

help:
	@echo "RAG LLM Knowledge Worker - Development Tasks"
	@echo "============================================"
	@echo "make install       - Install dependencies"
	@echo "make dev-install   - Install dev dependencies"
	@echo "make test          - Run tests"
	@echo "make lint          - Run linters"
	@echo "make format        - Format code"
	@echo "make clean         - Clean build artifacts"
	@echo "make run           - Run main application"
	@echo "make docs          - Build documentation"

install:
	pip install -r requirements.txt

dev-install:
	pip install -r requirements.txt
	pip install pytest pytest-cov black flake8 mypy

test:
	pytest tests/ -v --cov=src

test-fast:
	pytest tests/ -v

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

format-check:
	black --check src/ tests/
	isort --check-only src/ tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info/

run:
	python main.py

example-basic:
	python examples/basic_usage.py

example-custom:
	python examples/custom_pipeline.py

example-advanced:
	python examples/advanced_features.py

docs:
	@echo "Documentation is in docs/ directory"
	@echo "Main files:"
	@echo "  - README.md - Project overview"
	@echo "  - docs/GETTING_STARTED.md - Getting started guide"
	@echo "  - docs/API_REFERENCE.md - API documentation"
	@echo "  - docs/ARCHITECTURE.md - System architecture"
	@echo "  - docs/INTEGRATION_GUIDE.md - Integration examples"

all: clean install test lint format
