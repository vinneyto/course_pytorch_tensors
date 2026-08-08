import torch
from task import pick_per_row


def test_gather():
    x = torch.tensor([[10, 11, 12], [20, 21, 22], [30, 31, 32]])
    assert torch.equal(pick_per_row(x, torch.tensor([2, 0, 1])), torch.tensor([12, 20, 31]))
    y = torch.arange(20).reshape(4, 5)
    assert torch.equal(pick_per_row(y, torch.tensor([4, 3, 2, 1])), torch.tensor([4, 8, 12, 16]))
