import torch
from task import repeat_column


def test_repeat_column_values_and_layout():
    x = torch.tensor([[1.0], [2.0], [3.0]])
    expanded, repeated = repeat_column(x, 4)
    expected = torch.tensor([[1.0] * 4, [2.0] * 4, [3.0] * 4])
    assert torch.equal(expanded, expected)
    assert torch.equal(repeated, expected)
    assert expanded.stride()[1] == 0
    assert repeated.is_contiguous()

    x[0, 0] = 99
    assert expanded[0, 2].item() == 99
    assert repeated[0, 2].item() == 1
