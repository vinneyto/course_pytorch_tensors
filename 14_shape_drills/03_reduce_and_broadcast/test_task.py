import torch
from task import center_last_axis


def test_reduce_and_broadcast():
    x = torch.randn(4, 7, 3)
    centered, mean = center_last_axis(x)
    assert mean.shape == (4, 7, 1) and centered.shape == x.shape
    assert torch.allclose(centered.mean(-1), torch.zeros(4, 7), atol=1e-6)
