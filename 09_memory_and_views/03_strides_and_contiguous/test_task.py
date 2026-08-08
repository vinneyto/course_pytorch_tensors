import pytest
import torch
from task import reorder_and_flatten


def test_layout():
    x = torch.arange(12).reshape(3, 4)
    y, strides, reshaped, contiguous_view = reorder_and_flatten(x)
    assert y.shape == (4, 3) and not y.is_contiguous()
    assert strides == (1, 4) and y.untyped_storage().data_ptr() == x.untyped_storage().data_ptr()
    expected = torch.tensor([0, 4, 8, 1, 5, 9, 2, 6, 10, 3, 7, 11])
    assert torch.equal(reshaped, expected) and torch.equal(contiguous_view, expected)
    with pytest.raises(RuntimeError):
        y.view(-1)
