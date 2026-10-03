import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    mu=float(sum(x))/float(len(x))
    final= float(sum([(x[i]-mu)**2 for i in range(0,len(x))]))
    variance=float(final/(len(x)-1))
    return {
        "variance":variance,
        "standard_deviation":float(np.sqrt(variance))
    }