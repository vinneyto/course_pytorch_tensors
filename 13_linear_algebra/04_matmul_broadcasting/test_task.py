import torch
from task import shared_vector_product


def test_matmul_broadcasting():
    for shape in [(4, 3, 3), (2, 5, 3)]:
        a, x = torch.randn(*shape), torch.randn(shape[-1])
        result = shared_vector_product(a, x)
        assert result.shape == shape[:-1] and torch.allclose(result, torch.matmul(a, x))
