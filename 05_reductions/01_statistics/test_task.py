import torch
from task import column_stats

def test_column_stats():
    x=torch.tensor([[1.,5.,3.],[3.,2.,9.]])
    means, maxima=column_stats(x)
    assert torch.allclose(means, torch.tensor([2.,3.5,6.]))
    assert torch.equal(maxima, torch.tensor([3.,5.,9.]))
