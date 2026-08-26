import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    x = np.asarray(x,dtype=float)
    y = np.asarray(y,dtype=float)
    total = 0
    for i,j in zip(x,y):
        total += abs(i-j)**2
    return np.sqrt(total)
        