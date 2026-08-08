import torch
from task import apply_matrix


def test_apply_matrix():
    matrix = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    vector = torch.tensor([10.0, 20.0, 30.0])
    result = apply_matrix(matrix, vector)
    assert result.shape == (2,)
    assert torch.equal(result, torch.tensor([140.0, 320.0]))
