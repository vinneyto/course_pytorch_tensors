import torch
from task import center_spatial


def test_center_spatial():
    x = torch.arange(2 * 3 * 4 * 2, dtype=torch.float32).reshape(2, 3, 4, 2)
    centered, means = center_spatial(x)
    assert means.shape == (2, 1, 1, 2)
    assert centered.shape == x.shape
    assert torch.allclose(centered.mean(dim=(1, 2)), torch.zeros(2, 2))
    assert torch.allclose(x - centered, means.expand_as(x))
