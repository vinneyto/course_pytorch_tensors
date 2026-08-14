import torch
from task import batched_diagonal


def test_batched_diagonal():
    for values, offset in [
        (torch.arange(6).reshape(2, 3), 0),
        (torch.arange(24, dtype=torch.float32).reshape(2, 3, 4), 1),
        (torch.tensor([[True, False], [False, True]]), -2),
    ]:
        result = batched_diagonal(values, offset)
        matrix_size = values.shape[-1] + abs(offset)

        assert result.shape == (*values.shape[:-1], matrix_size, matrix_size)
        assert result.dtype == values.dtype
        assert result.device == values.device
        assert torch.equal(result, torch.diag_embed(values, offset=offset))
