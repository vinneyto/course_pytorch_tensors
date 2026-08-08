import torch


def channel_first(x: torch.Tensor) -> torch.Tensor:
    """Преобразовать HWC в NCHW."""
    return x.permute(2, 0, 1).unsqueeze(0)
