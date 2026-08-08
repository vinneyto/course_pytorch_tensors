import torch
from task import read_shapes


def test_index_and_permute():
    x = torch.randn(10, 20, 3)
    channel, chw = read_shapes(x)
    assert channel.shape == (10, 20) and torch.equal(channel, x[:, :, 0])
    assert chw.shape == (3, 10, 20) and torch.equal(chw[2], x[:, :, 2])
