import torch
from task import signed_square


def test_where():
    for x in [torch.tensor([-3.0, -1.0, 0.0, 2.0]), torch.randn(2, 3)]:
        before = x.clone()
        result = signed_square(x)
        expected = torch.where(x >= 0, x.square(), -x.square())
        assert torch.equal(result, expected) and torch.equal(x, before)
