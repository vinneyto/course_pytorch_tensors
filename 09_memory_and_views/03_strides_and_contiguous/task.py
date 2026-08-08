import torch


def reorder_and_flatten(x: torch.Tensor) -> tuple[torch.Tensor, tuple[int, ...], torch.Tensor, torch.Tensor]:
    """Переставить оси и показать два безопасных способа flatten."""
    raise NotImplementedError
