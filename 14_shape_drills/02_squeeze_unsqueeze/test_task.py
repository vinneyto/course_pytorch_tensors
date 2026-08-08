import torch
from task import make_column_batch


def test_make_column_batch():
    x = torch.arange(12).reshape(4, 3)
    expanded, squeezed = make_column_batch(x)
    assert expanded.shape == (4, 1, 3, 1)
    assert squeezed.shape == (4, 1, 3)
    assert torch.equal(squeezed[:, 0], x)
