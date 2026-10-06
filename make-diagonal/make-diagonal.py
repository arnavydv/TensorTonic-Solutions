import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    a=np.zeros((len(v),len(v)),dtype=float)
    for i in range(len(v)):
        a[i][i]=v[i]
    return a