import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    rng = np.random.default_rng(seed)
    bootstrap_means = []

    for _ in range(n_bootstrap):
        sample = rng.choice(x,size=len(x),replace=True)
        bootstrap_means.append(np.mean(sample))

    bootstrap_means = np.array(bootstrap_means)
    bootstrap_mean = np.mean(bootstrap_means)

    alpha = (1-ci)/2

    lower = np.quantile(bootstrap_means,alpha)
    upper = np.quantile(bootstrap_means,1-alpha)

    return {
        "bootstrap_mean":float(bootstrap_mean),
        "lower":float(lower),
        "upper":float(upper)
    }