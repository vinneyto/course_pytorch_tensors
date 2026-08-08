import torch
from task import spatial_mean


def test_multiple_axes():
    for shape in [(2, 3, 4, 5), (1, 2, 7, 3)]:
        x = torch.arange(torch.tensor(shape).prod()).reshape(shape).float()
        result = spatial_mean(x)
        assert result.shape == (shape[0], shape[3])
        assert torch.allclose(result, x.mean(dim=(1, 2)))
