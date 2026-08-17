import torch


def describe_like(x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Создать нули и булеву маску, подобные входу."""
    return (torch.zeros_like(x), torch.ones_like(x).to(torch.bool))
