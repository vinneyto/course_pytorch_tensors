import torch


def stack_steps(steps: list[torch.Tensor]) -> torch.Tensor:
    """Собрать шаги времени в новую ось после batch-оси."""
    raise NotImplementedError
