import torch
from task import make_grid


def test_make_grid():
    zeros, ones, grid = make_grid(2, 3)
    assert zeros.shape == (2, 3) and torch.count_nonzero(zeros) == 0
    assert torch.equal(ones, torch.ones(3))
    assert torch.equal(grid, torch.tensor([[0, 1, 2], [3, 4, 5]]))
    assert grid.dtype == torch.int64
