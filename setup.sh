#!/bin/bash

# Setup script for RAG LLM project

echo "=========================================="
echo "RAG LLM - Setup Script"
echo "=========================================="

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Create data directories
echo ""
echo "Creating data directories..."
mkdir -p data/documents
mkdir -p data/vector_store
mkdir -p logs

# Copy environment file
echo ""
echo "Setting up environment variables..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file. Please edit it with your API keys."
else
    echo ".env file already exists."
fi

# Create initial test document
echo ""
echo "Creating sample documents..."
if [ ! -f data/documents/welcome.txt ]; then
    cat > data/documents/welcome.txt << EOL
Welcome to RAG LLM

This is a sample document to get you started with the RAG LLM system.

RAG (Retrieval-Augmented Generation) combines the power of large language models
with a retrieval system to provide accurate, contextual responses based on your
private knowledge base.

To get started:
1. Add your documents to the data/documents/ directory
2. Build the knowledge base: python src/main.py build data/documents
3. Query the system: python src/main.py query "Your question here"

Enjoy building your private knowledge worker!
EOL
    echo "Created sample document: data/documents/welcome.txt"
fi

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your API keys"
echo "2. Add documents to data/documents/"
echo "3. Run: python src/main.py build data/documents"
echo "4. Query: python src/main.py query 'Your question'"
echo ""
echo "For more information, see README.md"
