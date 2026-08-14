import torch


def column_stats(x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Средние и максимумы по столбцам."""
    return (x.mean(0), x.amax(0))
