import torch


def euclidean(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """Вычислить скалярное евклидово расстояние."""
    return torch.sqrt(torch.sum((a - b) ** 2))
