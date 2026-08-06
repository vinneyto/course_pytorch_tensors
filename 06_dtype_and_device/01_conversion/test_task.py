import torch
from task import as_probabilities

def test_probabilities():
    x=torch.tensor([1,2,1], dtype=torch.int64)
    result=as_probabilities(x)
    assert result.dtype == torch.float32 and result.device == x.device
    assert torch.allclose(result, torch.tensor([.25,.5,.25]))
    assert x.dtype == torch.int64
