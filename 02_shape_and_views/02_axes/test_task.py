import torch
from task import channel_first


def test_channel_first():
    x = torch.arange(24).reshape(2, 4, 3)
    result = channel_first(x)
    assert result.shape == (1, 3, 2, 4)
    assert torch.equal(result[0, :, 1, 2], x[1, 2, :])
