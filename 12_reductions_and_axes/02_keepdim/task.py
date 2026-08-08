import torch


def center_spatial(x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Центрировать каждый канал изображения по пространственным осям."""
    raise NotImplementedError
