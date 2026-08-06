import torch

def clip_negatives(x: torch.Tensor, limit: float) -> tuple[torch.Tensor, torch.Tensor]:
    """Обнулить отрицательные значения в копии и выбрать большие."""
    raise NotImplementedError
