import torch
from task import spatial_mean


def test_spatial_mean():
    x = torch.arange(2 * 3 * 4 * 2, dtype=torch.float32).reshape(2, 3, 4, 2)
    result = spatial_mean(x)
    assert result.shape == (2, 2)
    assert torch.allclose(result[0], x[0].reshape(-1, 2).mean(dim=0))
    assert torch.allclose(result[1], x[1].reshape(-1, 2).mean(dim=0))
