import torch
from task import describe_like

def test_describe_like():
    x=torch.randn(2,3,dtype=torch.float64)
    zeros, mask=describe_like(x)
    assert zeros.shape == x.shape and zeros.dtype == x.dtype and zeros.device == x.device
    assert torch.count_nonzero(zeros) == 0
    assert mask.shape == x.shape and mask.dtype == torch.bool and torch.all(mask)
