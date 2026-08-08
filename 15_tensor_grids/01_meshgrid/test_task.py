import torch
from task import pixel_grid


def test_pixel_grid():
    grid, flat = pixel_grid(4, 3)
    assert grid.shape == (3, 4, 2)
    assert flat.shape == (12, 2)
    assert torch.equal(grid[0, 0], torch.tensor([0, 0]))
    assert torch.equal(grid[0, 3], torch.tensor([3, 0]))
    assert torch.equal(grid[2, 1], torch.tensor([1, 2]))
    assert torch.equal(flat[:5], torch.tensor([[0, 0], [1, 0], [2, 0], [3, 0], [0, 1]]))
