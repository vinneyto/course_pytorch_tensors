import torch
from task import axis_variants


def test_axis_variants_shapes():
    x = torch.arange(10 * 20 * 3, dtype=torch.float32).reshape(10, 20, 3)
    with_axis, first_channel, means, permuted = axis_variants(x)
    assert with_axis.shape == (10, 1, 20, 3)
    assert first_channel.shape == (10, 20)
    assert means.shape == (10, 20, 1)
    assert permuted.shape == (3, 10, 20)
    assert torch.equal(first_channel, x[:, :, 0])
