#!/usr/bin/env python3
"""
OpenAI Embedding Utilities
Provides utilities for creating and using OpenAI embedding models.
"""

import os
import openai
from typing import List, Union, Tuple
import numpy as np
import time
import logging
from pathlib import Path
from dotenv import load_dotenv
import tiktoken

# Load environment variables from .env file in the project root
project_root = Path(__file__).parent.parent
env_file = project_root / '.env'
if env_file.exists():
    load_dotenv(env_file)
    print(f"Loaded environment variables from {env_file}")
else:
    print(f"Warning: .env file not found at {env_file}")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpenAIEmbeddingModel:
    """Wrapper class for OpenAI embedding models that mimics sentence-transformers interface."""
    
    def __init__(self, model_name: str = "text-embedding-3-large"):
        self.model_name = model_name
        self.client = openai.OpenAI()
        self.max_tokens = 8192  # Maximum tokens for text-embedding-3-large
        
        # Initialize tokenizer for token counting
        try:
            self.tokenizer = tiktoken.encoding_for_model("text-embedding-3-large")
        except:
            # Fallback to cl100k_base encoding if model-specific tokenizer not available
            self.tokenizer = tiktoken.get_encoding("cl100k_base")
        
        # Verify API key is set
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable must be set")
        
        logger.info(f"Initialized OpenAI embedding model: {model_name}")
    
    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in a text."""
        return len(self.tokenizer.encode(text))
    
    def truncate_text(self, text: str, max_tokens: int = None) -> str:
        """Truncate text to fit within token limits."""
        if max_tokens is None:
            max_tokens = self.max_tokens - 10  # Leave some buffer
        
        tokens = self.tokenizer.encode(text)
        if len(tokens) <= max_tokens:
            return text
        
        # Truncate and decode back to text
        truncated_tokens = tokens[:max_tokens]
        truncated_text = self.tokenizer.decode(truncated_tokens)
        return truncated_text + "... [TRUNCATED]"
    
    def encode(self, texts: Union[str, List[str]], show_progress_bar: bool = True, batch_size: int = 100) -> np.ndarray:
        """
        Encode texts into embeddings using OpenAI API.
        
        Args:
            texts: Single text or list of texts to encode
            show_progress_bar: Whether to show progress (not used, kept for compatibility)
            batch_size: Number of texts to process in each batch
            
        Returns:
            numpy array of embeddings
        """
        if isinstance(texts, str):
            texts = [texts]
        
        # Process texts to handle token limits
        processed_texts = []
        skipped_count = 0
        
        for i, text in enumerate(texts):
            token_count = self.count_tokens(text)
            
            if token_count > self.max_tokens:
                # Truncate text that's too long
                truncated_text = self.truncate_text(text)
                processed_texts.append(truncated_text)
                if i < 5:  # Only log first few truncations to avoid spam
                    logger.warning(f"Text {i+1} truncated from {token_count} to {self.count_tokens(truncated_text)} tokens")
            else:
                processed_texts.append(text)
        
        if skipped_count > 0:
            logger.warning(f"Skipped {skipped_count} texts that were too long")
        
        embeddings = []
        total = len(processed_texts)
        
        for i in range(0, total, batch_size):
            batch = processed_texts[i:i + batch_size]
            
            # Calculate total tokens in batch to avoid batch-level limits
            batch_total_tokens = sum(self.count_tokens(text) for text in batch)
            
            # If batch is too large, reduce batch size
            if batch_total_tokens > self.max_tokens * 0.8 * len(batch):  # Conservative estimate
                # Process one by one for this batch
                for single_text in batch:
                    try:
                        response = self.client.embeddings.create(
                            input=[single_text],
                            model=self.model_name
                        )
                        embeddings.extend([data.embedding for data in response.data])
                        time.sleep(0.1)  # Rate limiting
                    except Exception as e:
                        logger.error(f"Error processing single text: {e}")
                        # Add zero embedding as placeholder
                        embeddings.append([0.0] * self.get_sentence_embedding_dimension())
            else:
                try:
                    response = self.client.embeddings.create(
                        input=batch,
                        model=self.model_name
                    )
                    
                    # Extract embeddings from response
                    batch_embeddings = [data.embedding for data in response.data]
                    embeddings.extend(batch_embeddings)
                    
                    if show_progress_bar and total > batch_size:
                        logger.info(f"Processed {min(i + batch_size, total)}/{total} texts")
                    
                    # Rate limiting - small delay between batches
                    if i + batch_size < total:
                        time.sleep(0.1)
                        
                except Exception as e:
                    logger.error(f"Error processing batch {i//batch_size + 1}: {e}")
                    # Add zero embeddings as placeholders
                    for _ in batch:
                        embeddings.append([0.0] * self.get_sentence_embedding_dimension())
        
        return np.array(embeddings)
    
    def get_sentence_embedding_dimension(self) -> int:
        """Get the dimension of embeddings for this model."""
        # Common dimensions for OpenAI models
        if "text-embedding-3-large" in self.model_name:
            return 3072
        elif "text-embedding-3-small" in self.model_name:
            return 1536
        elif "text-embedding-ada-002" in self.model_name:
            return 1536
        else:
            # Default, but should be verified
            return 1536


def create_openai_embedding_model(model_name: str = "text-embedding-3-large") -> OpenAIEmbeddingModel:
    """
    Create an OpenAI embedding model instance.
    
    Args:
        model_name: Name of the OpenAI embedding model to use
        
    Returns:
        OpenAIEmbeddingModel instance
    """
    return OpenAIEmbeddingModel(model_name)


def estimate_cost(num_texts: int, avg_tokens_per_text: int = 500, model_name: str = "text-embedding-3-large") -> float:
    """
    Estimate the cost of embedding generation.
    
    Args:
        num_texts: Number of texts to embed
        avg_tokens_per_text: Average number of tokens per text
        model_name: OpenAI model name
        
    Returns:
        Estimated cost in USD
    """
    total_tokens = num_texts * avg_tokens_per_text
    
    # Pricing as of 2024 (may change)
    pricing = {
        "text-embedding-3-large": 0.00013 / 1000,  # $0.00013 per 1K tokens
        "text-embedding-3-small": 0.00002 / 1000,  # $0.00002 per 1K tokens
        "text-embedding-ada-002": 0.0001 / 1000,   # $0.0001 per 1K tokens
    }
    
    price_per_token = pricing.get(model_name, 0.0001 / 1000)  # Default to ada-002 pricing
    return total_tokens * price_per_token
