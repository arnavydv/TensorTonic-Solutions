import numpy as np

def gradient_descent_step(values: list, gradients: list, learning_rate: float) -> tuple[list, float]:
    updated_list=[]
    for i in range(0,len(values)):
        new_val=values[i]-(learning_rate*gradients[i])
        new_val=float(new_val)
        updated_list.append(new_val)
    val=float(-learning_rate*sum([i**2 for i in gradients]))
    return updated_list,val
