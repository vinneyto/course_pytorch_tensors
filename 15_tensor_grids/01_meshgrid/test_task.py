import torch
from task import pixel_grid


def test_meshgrid():
    for height, width in [(2, 3), (4, 1)]:
        grid_x, grid_y, coordinates = pixel_grid(height, width)
        assert grid_x.shape == grid_y.shape == (height, width)
        assert coordinates.shape == (height * width, 2)
        assert torch.equal(coordinates[0], torch.tensor([0, 0]))
        assert torch.equal(coordinates[-1], torch.tensor([width - 1, height - 1]))
        assert torch.equal(coordinates, torch.stack((grid_x, grid_y), dim=-1).reshape(-1, 2))
