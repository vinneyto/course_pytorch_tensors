import torch
from task import diagonal_roundtrip


def test_diagonal_roundtrip():
    for values, offset in [
        (torch.tensor([1, 2, 3]), 0),
        (torch.tensor([1.5, -2.0]), 2),
        (torch.tensor([True, False, True, True]), -1),
    ]:
        matrix, restored = diagonal_roundtrip(values, offset)
        size = values.numel() + abs(offset)

        assert matrix.shape == (size, size)
        assert matrix.dtype == values.dtype
        assert matrix.device == values.device
        assert torch.equal(matrix, torch.diag(values, diagonal=offset))
        assert torch.equal(restored, values)
