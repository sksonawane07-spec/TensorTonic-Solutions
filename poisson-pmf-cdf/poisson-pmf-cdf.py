import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    cdf = 0
    for i in range(k + 1):
        pmf = (math.exp(-lam)*lam**i)/math.factorial(i)
        cdf += pmf
        
    return {
        'pmf':pmf,
        'cdf':cdf
    }