import torch
from task import center_rows

def test_center_rows():
    x=torch.tensor([[1.,2.,3.],[10.,20.,30.]])
    result=center_rows(x)
    assert torch.allclose(result, torch.tensor([[-1.,0.,1.],[-10.,0.,10.]]))
    assert torch.allclose(result.mean(dim=1), torch.zeros(2))
