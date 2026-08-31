import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    arr = np.array(X)
    mean = np.mean(arr,axis=0)
    x1 =  arr - mean
    N = arr.shape[0]
    return (x1.T @ x1)/(N - 1) 