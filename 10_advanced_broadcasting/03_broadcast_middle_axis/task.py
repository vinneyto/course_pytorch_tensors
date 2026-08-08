import torch


def add_sequence_bias(sequence: torch.Tensor, bias: torch.Tensor) -> torch.Tensor:
    """Добавить bias каждого объекта ко всем его временным шагам."""
    raise NotImplementedError
