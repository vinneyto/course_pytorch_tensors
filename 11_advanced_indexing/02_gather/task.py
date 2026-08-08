import torch


def pick_per_row(x: torch.Tensor, indices: torch.Tensor) -> torch.Tensor:
    """Выбрать по одному элементу из каждой строки через gather."""
    raise NotImplementedError
