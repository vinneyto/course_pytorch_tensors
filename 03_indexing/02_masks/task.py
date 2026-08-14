import torch


def clip_negatives(x: torch.Tensor, limit: float) -> tuple[torch.Tensor, torch.Tensor]:
    """Обнулить отрицательные значения в копии и выбрать большие."""
    x_copy = x.clone()
    x_copy[x_copy < 0] = 0

    return (x_copy, torch.masked_select(x, x > limit))
