import torch


def channel_summary(x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Проследить shapes BHWC -> BCHW -> BC(HW) -> BC1."""
    raise NotImplementedError
