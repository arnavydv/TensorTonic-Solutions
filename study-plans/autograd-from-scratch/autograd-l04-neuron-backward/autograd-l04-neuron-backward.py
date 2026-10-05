import torch

def neuron_backward(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor, upstream_gradient: torch.Tensor) -> tuple:
    """
    Returns a tuple of tensors: output, input gradients, weight gradients, bias gradient.
    """
    linear_output = torch.dot(inputs, weights) + bias
    activation_output = torch.tanh(linear_output)
    local_act_grad = 1.0 - activation_output ** 2
    grad = upstream_gradient * local_act_grad
    d_inputs = grad * weights
    d_weights = grad * inputs
    d_bias = grad.clone() 
    return activation_output, d_inputs, d_weights, d_bias
