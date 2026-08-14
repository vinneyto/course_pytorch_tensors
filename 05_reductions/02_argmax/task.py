import torch


def best_in_each_row(scores: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Вернуть индексы и значения победителей строк."""
    # indices = scores.argmax(1)
    # values = scores.gather(1, indices.unsqueeze(-1)).squeeze(1)
    values, indices = scores.max(1)

    return (indices, values)
