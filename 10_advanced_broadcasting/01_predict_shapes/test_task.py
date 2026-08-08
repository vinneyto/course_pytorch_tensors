import torch
from task import broadcast_examples


def test_broadcast_examples():
    a, b = torch.randn(3, 1, 5), torch.randn(1, 4, 1)
    c, d = torch.randn(8, 3, 1), torch.randn(1, 5)
    first, second, built = broadcast_examples(a, b, c, d)
    assert first.shape == (3, 4, 5) and torch.allclose(first, a + b)
    assert second.shape == (8, 3, 5) and torch.allclose(second, c + d)
    assert built.shape == (3, 4, 5) and torch.all(built == 2)
