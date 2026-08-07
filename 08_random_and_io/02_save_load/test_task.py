import torch
from task import load_pair, save_pair


def test_round_trip(tmp_path):
    x = torch.arange(4)
    y = torch.eye(2)
    path = tmp_path / "pair.pt"
    save_pair(path, x, y)
    assert path.is_file()
    loaded_x, loaded_y = load_pair(path)
    assert torch.equal(loaded_x, x) and torch.equal(loaded_y, y)
