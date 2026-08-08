import torch
from task import add_group_axis


def test_add_axis():
    x = torch.randn(10, 20, 3)
    result = add_group_axis(x)
    assert result.shape == (10, 1, 20, 3) and torch.equal(result[:, 0], x)
