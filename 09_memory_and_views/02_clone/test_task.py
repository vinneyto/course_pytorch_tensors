import torch
from task import view_and_copy


def test_view_and_copy():
    x = torch.arange(24).reshape(4, 6)
    view, copy = view_and_copy(x)
    assert torch.equal(view, x[:, 1:-1]) and torch.equal(copy, view)
    view[0, 0] = -10
    assert x[0, 1] == -10
    copy[1, 1] = -20
    assert x[1, 2] != -20
