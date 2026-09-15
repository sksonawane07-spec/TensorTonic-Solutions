import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    # Write code here
    pmf  = []
    for i in k:
        result = (1-p)**(i-1)*p
        pmf.append(result)

    mean = 1/p
    return {
        'pmf':np.array(pmf),
        'mean':mean
    }