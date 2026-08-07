import torch


def make_grid(rows: int, cols: int) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Создать нули, единицы и последовательную сетку."""
    zeros = torch.zeros((rows, cols))
    ones = torch.ones(cols)
    grid = torch.arange(rows * cols).reshape((rows, cols))

    return (zeros, ones, grid)
