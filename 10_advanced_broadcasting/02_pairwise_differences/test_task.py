import torch
from task import pairwise_differences


def test_pairwise_differences():
    for n, m, d in [(2, 4, 3), (5, 1, 2)]:
        points = torch.arange(n * d).reshape(n, d)
        queries = torch.arange(m * d).reshape(m, d) * 2
        result = pairwise_differences(points, queries)
        assert result.shape == (n, m, d)
        assert torch.equal(result[1, m - 1], points[1] - queries[m - 1])
