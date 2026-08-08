import torch
from task import pairwise_differences


def test_pairwise_differences():
    points = torch.tensor([[1.0, 2.0], [10.0, 20.0]])
    queries = torch.tensor([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
    result = pairwise_differences(points, queries)
    assert result.shape == (2, 3, 2)
    assert torch.equal(result[0, 2], torch.tensor([-3.0, -3.0]))
    assert torch.equal(result[1, 1], torch.tensor([8.0, 17.0]))


def test_pairwise_differences_three_coordinates():
    points = torch.arange(12.0).reshape(4, 3)
    queries = torch.arange(6.0).reshape(2, 3)
    result = pairwise_differences(points, queries)
    assert result.shape == (4, 2, 3)
    assert torch.equal(result[:, 0, :], points - queries[0])
