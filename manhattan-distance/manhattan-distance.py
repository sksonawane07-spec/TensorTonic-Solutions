import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    result = 0
    for i,j in zip(x,y):
        result += abs(i - j)
    return float(result)