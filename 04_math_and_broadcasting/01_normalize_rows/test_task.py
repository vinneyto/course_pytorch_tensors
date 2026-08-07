import torch
from task import center_rows


def test_center_rows():
    x = torch.tensor([[1.0, 2.0, 3.0], [10.0, 20.0, 30.0]])
    result = center_rows(x)
    assert torch.allclose(result, torch.tensor([[-1.0, 0.0, 1.0], [-10.0, 0.0, 10.0]]))
    assert torch.allclose(result.mean(dim=1), torch.zeros(2))
