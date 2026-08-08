import torch
from task import batched_matrix_vector


def test_batched_matmul():
    for batch in (1, 4):
        a, x = torch.randn(batch, 3, 3), torch.randn(batch, 3, 1)
        result = batched_matrix_vector(a, x)
        assert result.shape == (batch, 3, 1) and torch.allclose(result, torch.bmm(a, x))
