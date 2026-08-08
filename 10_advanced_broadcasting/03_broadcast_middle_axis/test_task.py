import torch
from task import add_sequence_bias


def test_middle_axis():
    sequence = torch.zeros(3, 5, 2)
    bias = torch.tensor([[1, 2], [3, 4], [5, 6]])
    result = add_sequence_bias(sequence, bias)
    assert result.shape == sequence.shape
    assert torch.equal(result[:, 0], bias) and torch.equal(result[:, -1], bias)
