import torch


def broadcast_shape(shape_a: tuple[int, ...], shape_b: tuple[int, ...]) -> torch.Size:
    """Вернуть общую broadcasting-форму."""
    raise NotImplementedError
