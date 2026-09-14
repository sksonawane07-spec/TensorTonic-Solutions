import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    x = np.sort(x)
    result = []
    n = len(x)
    for percentiles in q:
        r = (percentiles/100)*(n-1)
        l = int(np.floor(r))
        u = int(np.ceil(r))
        w = r - l
        value = (1-w)*x[l]+w*x[u]
        result.append(value)
    return np.array(result)