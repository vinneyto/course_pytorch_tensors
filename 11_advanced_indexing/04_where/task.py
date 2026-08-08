import torch


def dead_zone(x: torch.Tensor, limit: float) -> torch.Tensor:
    """Обнулить значения внутри симметричной dead zone."""
    raise NotImplementedError
