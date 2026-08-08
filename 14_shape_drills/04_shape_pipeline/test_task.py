import torch
from task import shape_pipeline


def test_shape_pipeline():
    x = torch.arange(2 * 5 * 3).reshape(2, 5, 3)
    result = shape_pipeline(x)
    assert result.shape == (2, 3) and torch.equal(result, x.sum(dim=1))
