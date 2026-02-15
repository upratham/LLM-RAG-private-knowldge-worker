"""
Data Ingestion Module - Load and process various document formats
"""

from .loader import DocumentLoader
from .pipeline import DataIngestionPipeline

__all__ = [
    "DocumentLoader",
    "DataIngestionPipeline",
]
