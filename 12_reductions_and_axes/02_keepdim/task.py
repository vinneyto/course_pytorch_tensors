import torch


def center_spatially(x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Центрировать каждый канал, сохранив reduction-оси."""
    raise NotImplementedError
