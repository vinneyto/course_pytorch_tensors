import torch
from task import view_and_copy


def test_view_and_copy_aliasing():
    x = torch.arange(20).reshape(4, 5)
    view, copy = view_and_copy(x)
    expected = x[:, 1:-1].clone()
    assert torch.equal(view, expected)
    assert torch.equal(copy, expected)

    view[0, 0] = -10
    assert x[0, 1].item() == -10
    assert copy[0, 0].item() != -10

    copy[1, 1] = -20
    assert x[1, 2].item() != -20
