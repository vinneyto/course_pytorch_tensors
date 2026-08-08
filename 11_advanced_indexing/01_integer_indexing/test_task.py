import torch
from task import select_rows


def test_select_rows_order_and_copy():
    x = torch.arange(20).reshape(5, 4)
    indices = torch.tensor([3, 0, 3, 1])
    result = select_rows(x, indices)
    expected = torch.stack([x[3], x[0], x[3], x[1]])
    assert torch.equal(result, expected)

    result[0, 0] = -100
    assert x[3, 0].item() != -100
