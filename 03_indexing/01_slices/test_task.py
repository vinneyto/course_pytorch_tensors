import torch
from task import interior_and_border

def test_slices():
    x=torch.arange(25).reshape(5,5)
    interior, top = interior_and_border(x)
    assert torch.equal(interior, torch.tensor([[6,7,8],[11,12,13],[16,17,18]]))
    assert torch.equal(top, torch.tensor([4,3,2,1,0]))
