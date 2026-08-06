from pathlib import Path
import torch

def save_pair(path: str | Path, x: torch.Tensor, y: torch.Tensor) -> None:
    """Сохранить пару тензоров в одном файле."""
    raise NotImplementedError

def load_pair(path: str | Path) -> tuple[torch.Tensor, torch.Tensor]:
    """Безопасно загрузить ранее сохранённую пару."""
    raise NotImplementedError
