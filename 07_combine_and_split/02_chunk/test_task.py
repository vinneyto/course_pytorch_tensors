import torch
from task import split_columns


def test_split_columns():
    x = torch.arange(12).reshape(2, 6)
    parts = split_columns(x, [1, 2, 3])
    assert tuple(p.shape for p in parts) == ((2, 1), (2, 2), (2, 3))
    assert torch.equal(torch.cat(parts, dim=1), x)
