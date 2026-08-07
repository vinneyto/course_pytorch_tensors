import torch


def make_tensors(values: list[float]) -> tuple[torch.Tensor, torch.Tensor]:
    """Создать независимые float32- и int64-тензоры из списка."""

    a = torch.tensor(values, dtype=torch.float32)
    b = torch.tensor(values, dtype=torch.int64)

    return (a, b)
