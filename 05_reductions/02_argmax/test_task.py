import torch
from task import best_in_each_row


def test_best():
    x = torch.tensor([[1.0, 8.0, 3.0], [9.0, 2.0, 4.0]])
    indices, values = best_in_each_row(x)
    assert torch.equal(indices, torch.tensor([1, 0]))
    assert torch.equal(values, torch.tensor([8.0, 9.0]))
    assert values.shape == (2,)
