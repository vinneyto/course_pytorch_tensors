import torch


def concat_features(left: torch.Tensor, right: torch.Tensor) -> torch.Tensor:
    """Объединить признаки объектов по оси признаков."""
    print(left)
    print(right)
    print(torch.cat((left, right), dim=1))
    return torch.cat((left, right), dim=1)
