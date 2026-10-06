import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    x=np.asarray(x)
    z=1/(1+np.exp(-1*x))
    return np.array(x*z)