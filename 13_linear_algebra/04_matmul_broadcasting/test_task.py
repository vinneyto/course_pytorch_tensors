import torch
from task import apply_shared_vector


def test_apply_shared_vector():
    matrices = torch.arange(24.0).reshape(2, 4, 3)
    vector = torch.tensor([1.0, 2.0, 3.0])
    result = apply_shared_vector(matrices, vector)
    assert result.shape == (2, 4)
    assert torch.equal(result[0], matrices[0] @ vector)
    assert torch.equal(result[1], matrices[1] @ vector)
