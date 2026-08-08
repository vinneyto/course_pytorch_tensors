import torch
from task import broadcast_add


def test_three_dimensional_broadcasting():
    a = torch.zeros(3, 1, 5)
    b = torch.ones(1, 4, 1)
    result = broadcast_add(a, b)
    assert result.shape == (3, 4, 5)
    assert torch.equal(result, torch.ones(3, 4, 5))


def test_missing_leading_dimension():
    a = torch.arange(24.0).reshape(8, 3, 1)
    b = torch.arange(5.0).reshape(1, 5)
    result = broadcast_add(a, b)
    assert result.shape == (8, 3, 5)
    assert torch.equal(result[2, 1], a[2, 1] + b[0])
