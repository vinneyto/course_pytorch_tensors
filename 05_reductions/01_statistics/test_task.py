import torch
from task import column_stats


def test_column_stats():
    x = torch.tensor([[1.0, 5.0, 3.0], [3.0, 2.0, 9.0]])
    means, maxima = column_stats(x)
    assert torch.allclose(means, torch.tensor([2.0, 3.5, 6.0]))
    assert torch.equal(maxima, torch.tensor([3.0, 5.0, 9.0]))
