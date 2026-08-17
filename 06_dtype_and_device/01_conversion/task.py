import torch


def as_probabilities(x: torch.Tensor) -> torch.Tensor:
    """Преобразовать значения в доли float32."""
    return x.to(torch.float32) / x.sum()
