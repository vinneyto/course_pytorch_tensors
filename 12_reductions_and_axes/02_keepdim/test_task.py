import torch
from task import center_spatially


def test_keepdim():
    x = torch.randn(3, 4, 2, 5)
    centered, mean = center_spatially(x)
    assert mean.shape == (3, 1, 1, 5) and centered.shape == x.shape
    assert torch.allclose(centered, x - mean)
    assert torch.allclose(centered.mean(dim=(1, 2)), torch.zeros(3, 5), atol=1e-6)
