import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Returns the sinusoidal position matrix.
    """
    pos = np.arange(seq_length)[:,np.newaxis]

    i = np.arange(0,d_model,2)

    angle = pos / (10000 ** ( i / d_model))

    encoding = np.zeros((seq_length,d_model))

    encoding[:,0::2] = np.sin(angle)
    encoding[:,1::2] = np.cos(angle)
    return encoding