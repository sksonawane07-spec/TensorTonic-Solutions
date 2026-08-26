import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    a = np.asarray(a,dtype=float)
    b = np.asarray(b,dtype=float)
    dot = a@b
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot/(norm_a*norm_b))
