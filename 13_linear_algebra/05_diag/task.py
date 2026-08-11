import torch


def diagonal_roundtrip(
    values: torch.Tensor, offset: int = 0
) -> tuple[torch.Tensor, torch.Tensor]:
    """Создать матрицу с заданной диагональю и извлечь её обратно."""
    raise NotImplementedError
