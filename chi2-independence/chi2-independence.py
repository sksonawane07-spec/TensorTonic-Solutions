import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    C = np.array(C,dtype=float)
    row_total = C.sum(axis=1)
    col_total = C.sum(axis=0)
    N = C.sum()
    expected = np.outer(row_total,col_total)/N
    chi2 = np.sum((C - expected) ** 2/ expected)

    return {
        "chi2":float(chi2),
        "expected":np.array(expected),
    }