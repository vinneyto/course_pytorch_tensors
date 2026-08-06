import torch
from task import sample

def test_sample():
    first=sample(42,(2,3)); second=sample(42,(2,3)); other=sample(43,(2,3))
    assert first.shape == (2,3)
    assert torch.equal(first,second)
    assert not torch.equal(first,other)
    assert torch.all((first>=0)&(first<1))
