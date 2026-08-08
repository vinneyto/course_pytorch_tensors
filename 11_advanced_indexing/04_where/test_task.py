import torch
from task import dead_zone


def test_dead_zone():
    x = torch.tensor([-3.0, -0.5, 0.0, 0.9, 2.0])
    original = x.clone()
    result = dead_zone(x, 1.0)
    assert torch.equal(result, torch.tensor([-3.0, 0.0, 0.0, 0.0, 2.0]))
    assert torch.equal(x, original)


def test_dead_zone_strict_boundary():
    x = torch.tensor([-1.0, 1.0])
    assert torch.equal(dead_zone(x, 1.0), x)
