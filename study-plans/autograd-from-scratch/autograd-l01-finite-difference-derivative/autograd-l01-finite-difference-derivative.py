import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    n=len(coefficients)
    function=0
    function_h=0
    for i in range(0,n):
        function+=(x**i)*(coefficients[i])
        function_h+=((x+h)**i)*(coefficients[i])
    return (float(function),float(function_h),float(function_h-function)/h)
    