import torch
from task import middle_columns


def test_middle_columns_is_view():
    x = torch.arange(20).reshape(4, 5)
    part = middle_columns(x)
    assert torch.equal(part, x[:, 1:-1])
    part[1, 1] = 999
    assert x[1, 2].item() == 999


def test_middle_columns_general_shape():
    x = torch.arange(18).reshape(3, 6)
    part = middle_columns(x)
    assert part.shape == (3, 4)
