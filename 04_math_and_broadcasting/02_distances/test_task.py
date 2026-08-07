import torch
from task import euclidean


def test_euclidean():
    result = euclidean(torch.tensor([1.0, 2.0]), torch.tensor([4.0, 6.0]))
    assert isinstance(result, torch.Tensor) and result.ndim == 0
    assert torch.allclose(result, torch.tensor(5.0))
