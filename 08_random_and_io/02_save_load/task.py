from pathlib import Path
import torch


def save_pair(path: str | Path, x: torch.Tensor, y: torch.Tensor) -> None:
    """Сохранить пару тензоров в одном файле."""
    torch.save({"x": x, "y": y}, path)


def load_pair(path: str | Path) -> tuple[torch.Tensor, torch.Tensor]:
    """Безопасно загрузить ранее сохранённую пару."""
    result = torch.load(path, weights_only=True)
    print(result)
    return (result["x"], result["y"])
