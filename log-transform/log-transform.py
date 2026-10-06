import math

def log_transform(values: list) -> list:
    """
    Returns the log1p-transformed values rounded to four decimals.
    """
    final=[]
    for i in (values):
     final.append(math.log(1+i))
    return final