import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    X = np.array(X)
    y = np.array(y)
    matrix = np.eye(X.shape[1])
    w = np.linalg.inv(
        X.T @ X + lam * matrix
    )@X.T @ y
    return w