import torch
from task import clip_negatives


def test_clip_negatives():
    x = torch.tensor([-2.0, 3.0, -1.0, 7.0, 2.0])
    cleaned, selected = clip_negatives(x, 2)
    assert torch.equal(cleaned, torch.tensor([0.0, 3.0, 0.0, 7.0, 2.0]))
    assert torch.equal(selected, torch.tensor([3.0, 7.0]))
    assert torch.equal(x, torch.tensor([-2.0, 3.0, -1.0, 7.0, 2.0]))
