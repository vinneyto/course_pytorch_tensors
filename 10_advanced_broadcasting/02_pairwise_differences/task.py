import torch


def pairwise_differences(points: torch.Tensor, queries: torch.Tensor) -> torch.Tensor:
    """Получить все разности points[n] - queries[m]."""
    raise NotImplementedError
