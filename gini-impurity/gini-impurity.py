import numpy as np

def gini_impurity(y_left: list, y_right: list) -> float:
    """
    Returns the impurity as a float.
    """
    def gini(y):
        if len(y) == 0:
            return 0.0
        _,counts = np.unique(y,return_counts=True)
        probabilities = counts/len(y)

        return 1 - np.sum(probabilities ** 2)

    n_left = len(y_left)
    n_right = len(y_right)
    n = n_left + n_right

    if n == 0:
        return 0.0

    gini_left = gini(y_left)
    gini_right = gini(y_right)

    weighted_gini = (
        (n_left / n) * gini_left
        + (n_right / n) * gini_right
    )

    return float(weighted_gini)