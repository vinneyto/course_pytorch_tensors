import torch
from task import matrix_product


def test_matrix_matrix():
    for m, k, n in [(2, 3, 4), (5, 2, 1)]:
        a, b = torch.randn(m, k), torch.randn(k, n)
        result = matrix_product(a, b)
        assert result.shape == (m, n) and torch.allclose(result, torch.matmul(a, b))
