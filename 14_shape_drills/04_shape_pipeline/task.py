import torch


def shape_pipeline(x: torch.Tensor) -> torch.Tensor:
    """Пройти transpose → unsqueeze → sum → squeeze."""
    raise NotImplementedError
