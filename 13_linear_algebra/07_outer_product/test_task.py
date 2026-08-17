import torch
from task import batched_outer


def test_batched_outer_values_and_shape():
    a = torch.tensor([[1.0, 2.0], [-1.0, 3.0]])
    b = torch.tensor([[4.0, 5.0, 6.0], [2.0, 0.0, -2.0]])

    result = batched_outer(a, b)

    expected = torch.stack([torch.outer(a[0], b[0]), torch.outer(a[1], b[1])])
    assert result.shape == (2, 2, 3)
    assert torch.equal(result, expected)


def test_batched_outer_supports_other_shapes():
    a = torch.randn(4, 3)
    b = torch.randn(4, 5)

    result = batched_outer(a, b)

    expected = a.unsqueeze(-1) * b.unsqueeze(-2)
    assert result.shape == (4, 3, 5)
    assert torch.allclose(result, expected)
