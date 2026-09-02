import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    mean = np.mean(x)
    n = len(x)

    total = 0

    for i in x:
        total += (i - mean) ** 2

    std = np.sqrt(total / (n - 1))

    if std == 0:
        if mean == mu0:
            return 0.0
        return float('inf') if mean > mu0 else float('-inf')

    return float((mean - mu0) / (std / np.sqrt(n)))