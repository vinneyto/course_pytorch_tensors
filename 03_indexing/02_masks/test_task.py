import torch
from task import clip_negatives

def test_clip_negatives():
    x=torch.tensor([-2., 3., -1., 7., 2.])
    cleaned, selected=clip_negatives(x, 2)
    assert torch.equal(cleaned, torch.tensor([0.,3.,0.,7.,2.]))
    assert torch.equal(selected, torch.tensor([3.,7.]))
    assert torch.equal(x, torch.tensor([-2.,3.,-1.,7.,2.]))
