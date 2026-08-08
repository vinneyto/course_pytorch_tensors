import torch
from task import edit_middle


def test_slice_is_view():
    x = torch.arange(20).reshape(4, 5)
    part = edit_middle(x, -1)
    assert part.shape == (4, 2)
    assert torch.equal(x[:, 1:3], torch.full((4, 2), -1))
    part[0, 0] = 99
    assert x[0, 1] == 99
