def scalar_expression_partials(a: float, b: float, c: float, h: float) -> tuple[float, float, float, float]:
    def d(a,b,c):
        return a*b+c
    da=d(a,b,c)
    d_a=(d(a+h,b,c)-da)/h
    d_b=(d(a,b+h,c)-da)/h
    d_c=(d(a,b,c+h)-da)/h
    
    return float(da),float(d_a),float(d_b),float(d_c)
