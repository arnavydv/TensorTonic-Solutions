import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    return float(sum([(y_pred1-y_true1)**2 for y_pred1,y_true1 in zip(y_pred,y_true)])/len(y_pred))