import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    z=[]
    for i in x:
        z.append(i if i>=0 else alpha*i) 
    return np.asarray(z)