import numpy as np
import pickle
from tqdm import tqdm
from typing import List
from pathlib import Path
from FlagEmbedding import BGEM3FlagModel

from src.utils.constants import Paths

def embed_and_save(model: BGEM3FlagModel, col: List[str], file_name: str, batch_size: int) -> None:
    """
    Generate embeddings for the given text data and save them to a file.

    Parameters:
    - model (BGEM3FlagModel): The desired BGEM3FlagModel model
    - col (List[str]): A list of strings to generate embeddings for.
    - file_name (str): The name of the file to save the embeddings to.
    - batch_size (int): The batch size for the inference

    Returns:
    - None
    """
    try:
        
        # Encode the text data
        embeddings = model.encode(col, 
        batch_size=batch_size,
        max_length=8192)['dense_vecs']
        
        # Replace '-' with zero vectors
        for i, string in enumerate(col):
            if string == '-':
                embeddings[i] = np.zeros(embeddings.shape[1])
        
        # Save embeddings to a file
        with open(Path(Paths.EMBEDDINGS_DATA_PATH) / file_name, 'wb') as file:
            pickle.dump(embeddings, file)
        
        print(f"Embeddings saved successfully to {file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

def compute_cosine_similarity_matrix(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Computes the cosine similarity matrix between two sets of vectors.
    
    Args:
        A (np.ndarray): First ndarray of size (n, 1024).
        B (np.ndarray): Second ndarray of size (d, 1024).
    
    Returns:
        np.ndarray: Cosine similarity matrix of size (n, d).
    """
    n, d = A.shape[0], B.shape[0]
    
    # Initialize the result matrix
    similarity_matrix = np.zeros((n, d))
    
    # Compute magnitudes of A and B vectors
    magnitude_A = np.linalg.norm(A, axis=1)
    magnitude_B = np.linalg.norm(B, axis=1)
    
    # Compute cosine similarity for each pair of vectors
    pbar = tqdm(range(n))
    for i in pbar:
        for j in range(d):
            # Compute dot product
            dot_product = np.dot(A[i], B[j])
            # Compute cosine similarity
            similarity_matrix[i, j] = dot_product / (magnitude_A[i] * magnitude_B[j])
    
    return similarity_matrix

def get_knn(similarity_matrix: np.ndarray, k: int) -> np.ndarray:
    """
    Get the indices of the k largest elements in each row of the similarity matrix.
    
    Args:
    similarity_matrix (np.ndarray): The similarity matrix of size (n, d).
    k (int): The number of largest elements to find.
    
    Returns:
    np.ndarray: An array of size (n, k) containing the indices of the k largest elements in each row.
    """
    # Number of rows
    n = similarity_matrix.shape[0]
    
    # Initialize the result array
    knn_indices = np.zeros((n, k), dtype=int)
    
    # Iterate over each row
    pbar =  tqdm(range(n))
    for i in pbar:
        # Get the indices that would sort the row in descending order
        sorted_indices = np.argsort(-similarity_matrix[i])
        
        # Select the top k indices
        knn_indices[i] = sorted_indices[:k]
    
    return knn_indices