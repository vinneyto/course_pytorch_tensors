import torch


def scale_channels(x: torch.Tensor, scales: torch.Tensor) -> torch.Tensor:
    """Применить индивидуальный scale каждого канала внутри batch."""
    raise NotImplementedError
