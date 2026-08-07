import torch
from task import to_batches


def test_to_batches():
    x = torch.arange(12)
    matrix, flat = to_batches(x, 4)
    assert matrix.shape == (3, 4)
    assert torch.equal(matrix, x.reshape(3, 4))
    assert flat.shape == (12,) and torch.equal(flat, x)
