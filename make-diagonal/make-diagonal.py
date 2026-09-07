import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    values = np.asarray(v)
    matrix = np.zeros((values.size,values.size), dtype=values.dtype)
    indices = np.arange(values.size)
    matrix[indices,indices] = values
    return matrix