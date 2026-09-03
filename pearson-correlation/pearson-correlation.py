import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X = np.array(X,dtype=float)
    N = X.shape[0]

    centered = X - np.mean(X,axis=0)

    covariance = centered.T @ centered/(N-1)

    std = np.sqrt(np.diag(covariance))

    denominator = np.outer(std, std)

    correlation = covariance / denominator
    return correlation
    