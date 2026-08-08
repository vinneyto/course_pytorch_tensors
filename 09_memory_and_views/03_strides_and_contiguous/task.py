import torch


def transpose_and_flatten(
    x: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """Сравнить non-contiguous permute, contiguous, view и reshape."""
    raise NotImplementedError
