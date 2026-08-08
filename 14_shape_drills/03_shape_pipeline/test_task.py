import torch
from task import channel_summary


def test_channel_summary():
    x = torch.arange(2 * 3 * 4 * 5, dtype=torch.float32).reshape(2, 3, 4, 5)
    channels_first, flattened, means = channel_summary(x)
    assert channels_first.shape == (2, 5, 3, 4)
    assert flattened.shape == (2, 5, 12)
    assert means.shape == (2, 5, 1)
    assert torch.allclose(means.squeeze(-1), x.mean(dim=(1, 2)))
