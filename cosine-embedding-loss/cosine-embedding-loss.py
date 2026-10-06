import math
import numpy as np

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    cos=np.dot(x1,x2)/(math.hypot(*x1)*math.hypot(*x2))
    return 1-cos if label==1 else max(0,cos-margin)