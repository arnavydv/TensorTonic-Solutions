def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    x=[x0]
    for i in range(steps):
        grad=float(a*2*x[i]+b)
        x.append(float(x[i]-lr*grad))
    return float(x[-1])
    