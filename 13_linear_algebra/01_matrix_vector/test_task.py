import torch
from task import matrix_vector


def test_matrix_vector():
    for size in (2, 3, 5):
        a, x = torch.randn(size, size), torch.randn(size)
        result = matrix_vector(a, x)
        assert result.shape == (size,) and torch.allclose(result, torch.mv(a, x))
