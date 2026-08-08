import torch
from task import select_rows


def test_integer_indexing_is_copy():
    x = torch.arange(20).reshape(5, 4)
    result = select_rows(x, torch.tensor([3, 0, 3]))
    assert torch.equal(result, x[[3, 0, 3]])
    result[0, 0] = -1
    assert x[3, 0] != -1
