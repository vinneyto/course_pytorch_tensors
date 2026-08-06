import torch
from task import best_in_each_row

def test_best():
    x=torch.tensor([[1.,8.,3.],[9.,2.,4.]])
    indices, values=best_in_each_row(x)
    assert torch.equal(indices, torch.tensor([1,0]))
    assert torch.equal(values, torch.tensor([8.,9.]))
    assert values.shape == (2,)
