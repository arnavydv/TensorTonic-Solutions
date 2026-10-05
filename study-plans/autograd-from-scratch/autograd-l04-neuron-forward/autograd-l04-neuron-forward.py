import torch

def neuron_forward(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor) -> tuple:
    a=torch.dot(inputs,weights)+bias
    return a,torch.tanh(a)
