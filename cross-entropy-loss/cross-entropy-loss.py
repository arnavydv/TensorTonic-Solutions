import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    loss=0
    for i,j in zip(y_true,y_pred):
            loss+=float(-1*np.log(j[i]))
    return float(loss/len(y_true))
    