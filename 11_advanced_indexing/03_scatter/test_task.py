import torch
from task import place_per_row


def test_scatter():
    values = torch.tensor([5.0, 7.0, 9.0])
    result = place_per_row(values, torch.tensor([2, 0, 1]), 4)
    expected = torch.tensor([[0, 0, 5, 0], [7, 0, 0, 0], [0, 9, 0, 0]])
    assert torch.equal(result, expected) and result.dtype == values.dtype
