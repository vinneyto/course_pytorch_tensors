import torch
from task import make_tensors


def test_make_tensors():
    values = [1, 2, 3]
    floats, integers = make_tensors(values)
    assert torch.equal(floats, torch.tensor([1.0, 2.0, 3.0]))
    assert floats.dtype == torch.float32
    assert torch.equal(integers, torch.tensor([1, 2, 3]))
    assert integers.dtype == torch.int64
    floats[0] = 99
    assert values == [1, 2, 3]
