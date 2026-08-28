import numpy as np

def sample_var_std(x: list) -> dict:
    mean = np.mean(x)

    squared_diff = [(i - mean) ** 2 for i in x]

    variance = sum(squared_diff)/(len(x)-1)

    standard_deviation = np.sqrt(variance)

    return {
        "variance":float(variance),
        "standard_deviation":float(standard_deviation)
    }