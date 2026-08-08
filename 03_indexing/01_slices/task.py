import torch


def interior_and_border(x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Получить центр матрицы и развёрнутую верхнюю границу."""
    return (x[1:-1, 1:-1], x[0].flip(0))
