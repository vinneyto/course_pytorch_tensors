import torch
from task import scale_channels


def test_scale_channels():
    x = torch.ones(2, 4, 3)
    scales = torch.tensor([[1.0, 2.0, 3.0], [10.0, 20.0, 30.0]])
    result = scale_channels(x, scales)
    assert result.shape == (2, 4, 3)
    assert torch.equal(result[0, 2], scales[0])
    assert torch.equal(result[1, 3], scales[1])


def test_scale_channels_nontrivial_values():
    x = torch.arange(12.0).reshape(2, 2, 3)
    scales = torch.tensor([[2.0, 3.0, 4.0], [5.0, 6.0, 7.0]])
    result = scale_channels(x, scales)
    assert torch.equal(result[:, 0, :], x[:, 0, :] * scales)
