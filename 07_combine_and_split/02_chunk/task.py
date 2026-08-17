import torch


def split_columns(x: torch.Tensor, sizes: list[int]) -> tuple[torch.Tensor, ...]:
    """Разбить матрицу по столбцам."""
    print(sizes)
    print(x)
    for t in x.split(sizes, dim=1):
        print(t)
    return x.split(sizes, dim=1)
