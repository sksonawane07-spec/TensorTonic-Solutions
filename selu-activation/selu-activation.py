import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    ls = []
    for i in x:
        if i > 0:
            ls.append(1.0507009873554804934193349852946*i)
        else:
            ls.append(1.0507009873554804934193349852946*1.6732632423543772848170429916717*(math.exp(i)-1))
    return ls