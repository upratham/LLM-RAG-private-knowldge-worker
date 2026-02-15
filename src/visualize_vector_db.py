"""
Vector database visualization utilities using t-SNE and Plotly.

This module provides functions to visualize high-dimensional vectors from a Chroma vector store
in 2D and 3D using t-SNE dimensionality reduction.
"""

import numpy as np
import plotly.graph_objects as go
from sklearn.manifold import TSNE
from typing import Dict, List, Optional


def prepare_visualization_data(vector_store, random_state: int = 42) -> tuple:
    """
    Prepare data from vector store for visualization.
    
    Args:
        vector_store: A Chroma vector store instance
        random_state: Random state for reproducibility
        
    Returns:
        Tuple of (vectors, documents, doc_types, metadatas)
    """
    result = vector_store._collection.get(
        include=['embeddings', 'documents', 'metadatas']
    )
    vectors = np.array(result['embeddings'])
    documents = result['documents']
    metadatas = result['metadatas']
    doc_types = [metadata['type'] for metadata in metadatas]
    
    return vectors, documents, doc_types, metadatas


def get_default_colors() -> Dict[str, str]:
    """
    Get default color mapping for document types.
    
    Returns:
        Dictionary mapping document types to colors
    """
    return {
        'extra cariculam': 'red',
        'internships': 'blue',
        'repo_summaries': 'green',
        'academic achievements': 'orange',
        'transcripts': 'purple',
        'resume': 'brown',
        'research_papers': 'pink',
        'research integrity course certificates': 'cyan'
    }


def map_colors(doc_types: List[str], colors: Optional[Dict[str, str]] = None) -> List[str]:
    """
    Map document types to colors.
    
    Args:
        doc_types: List of document types
        colors: Dictionary mapping document types to colors. 
                If None, uses default colors.
        
    Returns:
        List of colors corresponding to each document type
    """
    if colors is None:
        colors = get_default_colors()
    
    return [colors.get(doc_type, 'gray') for doc_type in doc_types]


def visualize_2d(
    vector_store,
    colors: Optional[Dict[str, str]] = None,
    random_state: int = 42,
    title: str = '2D Chroma Vector Store Visualization',
    width: int = 800,
    height: int = 600
) -> go.Figure:
    """
    Visualize vector store in 2D using t-SNE.
    
    Args:
        vector_store: A Chroma vector store instance
        colors: Dictionary mapping document types to colors.
                If None, uses default colors.
        random_state: Random state for t-SNE reproducibility
        title: Title for the visualization
        width: Figure width in pixels
        height: Figure height in pixels
        
    Returns:
        Plotly Figure object
    """
    # Prepare data
    vectors, documents, doc_types, _ = prepare_visualization_data(
        vector_store, random_state
    )
    
    # Reduce dimensionality
    tsne = TSNE(n_components=2, random_state=random_state)
    reduced_vectors = tsne.fit_transform(vectors)
    
    # Map colors
    marker_colors = map_colors(doc_types, colors)
    
    # Create scatter plot
    fig = go.Figure(data=[go.Scatter(
        x=reduced_vectors[:, 0],
        y=reduced_vectors[:, 1],
        mode='markers',
        marker=dict(size=5, color=marker_colors, opacity=0.8),
        text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
        hoverinfo='text'
    )])
    
    fig.update_layout(
        title=title,
        xaxis_title='x',
        yaxis_title='y',
        width=width,
        height=height,
        margin=dict(r=20, b=10, l=10, t=40)
    )
    
    return fig


def visualize_3d(
    vector_store,
    colors: Optional[Dict[str, str]] = None,
    random_state: int = 42,
    title: str = '3D Chroma Vector Store Visualization',
    width: int = 900,
    height: int = 700
) -> go.Figure:
    """
    Visualize vector store in 3D using t-SNE.
    
    Args:
        vector_store: A Chroma vector store instance
        colors: Dictionary mapping document types to colors.
                If None, uses default colors.
        random_state: Random state for t-SNE reproducibility
        title: Title for the visualization
        width: Figure width in pixels
        height: Figure height in pixels
        
    Returns:
        Plotly Figure object
    """
    # Prepare data
    vectors, documents, doc_types, _ = prepare_visualization_data(
        vector_store, random_state
    )
    
    # Reduce dimensionality
    tsne = TSNE(n_components=3, random_state=random_state)
    reduced_vectors = tsne.fit_transform(vectors)
    
    # Map colors
    marker_colors = map_colors(doc_types, colors)
    
    # Create 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=reduced_vectors[:, 0],
        y=reduced_vectors[:, 1],
        z=reduced_vectors[:, 2],
        mode='markers',
        marker=dict(size=5, color=marker_colors, opacity=0.8),
        text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
        hoverinfo='text'
    )])
    
    fig.update_layout(
        title=title,
        scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
        width=width,
        height=height,
        margin=dict(r=10, b=10, l=10, t=40)
    )
    
    return fig
