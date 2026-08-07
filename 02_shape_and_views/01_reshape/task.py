import torch


def to_batches(x: torch.Tensor, width: int) -> tuple[torch.Tensor, torch.Tensor]:
    """Изменить форму в 2D и обратно."""
    raise NotImplementedError
