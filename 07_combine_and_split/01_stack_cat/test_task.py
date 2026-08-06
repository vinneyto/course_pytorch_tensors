import torch
from task import combine

def test_combine():
    a,b=torch.tensor([1,2]),torch.tensor([3,4])
    stacked, concatenated=combine(a,b)
    assert torch.equal(stacked, torch.tensor([[1,2],[3,4]]))
    assert torch.equal(concatenated, torch.tensor([1,2,3,4]))
