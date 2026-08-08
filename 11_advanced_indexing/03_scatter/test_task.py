import torch
from task import place_values


def test_place_values():
    values = torch.tensor([5.0, 7.0, 9.0])
    indices = torch.tensor([2, 0, 3])
    result = place_values(values, indices, 4)
    expected = torch.tensor([[0.0, 0.0, 5.0, 0.0], [7.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 9.0]])
    assert torch.equal(result, expected)
    assert result.dtype == values.dtype
    assert result.device == values.device
