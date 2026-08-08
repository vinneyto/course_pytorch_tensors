import torch
from task import outer_sum_per_batch


def test_outer_sum_per_batch():
    a = torch.tensor([[1.0, 2.0], [10.0, 20.0]])
    b = torch.tensor([[3.0, 4.0, 5.0], [30.0, 40.0, 50.0]])
    result = outer_sum_per_batch(a, b)
    assert result.shape == (2, 2, 3)
    assert torch.equal(result[0], torch.tensor([[4.0, 5.0, 6.0], [5.0, 6.0, 7.0]]))
    assert torch.equal(result[1, 1], torch.tensor([50.0, 60.0, 70.0]))
