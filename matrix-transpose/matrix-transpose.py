import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    A = np.array(A)
    transpose = []

    for i in range(len(A[0])):
        row = []

        for j in range(len(A)):
            row.append(A[j][i])

        transpose.append(row)

    return np.array(transpose)