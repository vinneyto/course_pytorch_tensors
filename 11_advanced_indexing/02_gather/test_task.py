import torch
from task import choose_columns


def test_choose_columns():
    x = torch.tensor([[10, 11, 12], [20, 21, 22], [30, 31, 32]])
    indices = torch.tensor([2, 0, 1])
    result = choose_columns(x, indices)
    assert torch.equal(result, torch.tensor([12, 20, 31]))


def test_choose_columns_other_width():
    x = torch.arange(20).reshape(4, 5)
    indices = torch.tensor([4, 3, 2, 1])
    result = choose_columns(x, indices)
    assert torch.equal(result, torch.tensor([4, 8, 12, 16]))
