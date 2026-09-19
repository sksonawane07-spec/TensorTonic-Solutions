import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    ls = []
    for i in x:
        if i > 0:
            ls.append(i)
        else:
            ls.append(alpha * (math.exp(i)-1))  
    return ls